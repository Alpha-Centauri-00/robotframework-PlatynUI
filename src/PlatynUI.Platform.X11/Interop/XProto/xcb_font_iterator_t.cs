namespace PlatynUI.Platform.X11.Interop.XCB;

public unsafe partial struct xcb_font_iterator_t
{
    [NativeTypeName("xcb_font_t *")]
    public uint* data;

    public int rem;

    public int index;
}
