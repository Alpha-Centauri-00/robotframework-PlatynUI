using System;
using System.CodeDom;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using Avalonia.Data.Converters;
using PlatynUI.Runtime;

namespace PlatynUI.Spy.Converters
{
    public class ValueToStringConverter : IValueConverter
    {
        private static string ToLiteral(object input)
        {
            using var writer = new StringWriter();
            using var provider = CodeDomProvider.CreateProvider("CSharp");

            provider.GenerateCodeFromExpression(new CodePrimitiveExpression(input), writer, null);
            return writer.ToString();
        }

        private static string? Converts(object? value)
        {
            try
            {
                if (value == null)
                    return "null";

                return value switch
                {
                    string
                    or bool
                    or char
                    or byte
                    or sbyte
                    or short
                    or ushort
                    or int
                    or uint
                    or long
                    or ulong
                    or float
                    or double
                    or decimal
                        => ToLiteral(value),
                    DateTime dt => dt.ToString("G"),
                    DateTimeOffset dto => dto.ToString("G"),
                    TimeSpan ts => ts.ToString(),

                    Point p => p.ToString(),
                    Rect r => r.ToString(),

                    Array a => $"[{string.Join(", ", a.OfType<object>().Select(Converts))}]",

                    _ => value.ToString(),
                };
            }
            catch (Exception ex)
            {
                return $"<Error: {ex.Message}>";
            }
        }

        public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (value == null || string.IsNullOrWhiteSpace(parameter as string))
                return null;

            return Converts(value.GetType().GetProperty((parameter as string)!)?.GetValue(value));
        }

        public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (value == null || string.IsNullOrWhiteSpace(parameter as string))
                return null;

            return value.GetType().GetProperty((parameter as string)!)?.GetValue(value);
        }
    }
}
