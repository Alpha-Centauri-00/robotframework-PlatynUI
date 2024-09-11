// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.ComponentModel.Composition;
using PlatynUI.Runtime.Core;

namespace PlatynUI.Runtime;

public class MouseDevice
{
    [Import]
    protected IMouseDevice? mouseDevice;

    private MouseDevice()
    {
        PlatynUiExtensions.ComposeParts(this);
    }

    private static MouseDevice? _instance;
    private static MouseDevice Instance => _instance ??= new MouseDevice();

    public static double GetDoubleClickTime()
    {
        return Instance.mouseDevice?.GetDoubleClickTime() ?? 0;
    }

    public static Size GetDoubleClickSize()
    {
        return Instance.mouseDevice?.GetDoubleClickSize() ?? new Size();
    }

    public static Point GetPosition()
    {
        return Instance.mouseDevice?.GetPosition() ?? new Point();
    }

    public static void Move(double x, double y)
    {
        Console.WriteLine($"Moving mouse to {x}, {y}");
        Console.WriteLine($"Mouse device: {Instance.mouseDevice != null}");
        Instance.mouseDevice?.Move(x, y);
    }

    public static void Press(int button)
    {
        Instance.mouseDevice?.Press((MouseButton)button);
    }

    public static void Release(int button)
    {
        Instance.mouseDevice?.Release((MouseButton)button);
    }
}
