namespace PlatynUI.Platform.X11.Interop.XCB;

public unsafe partial struct xcb_bool32_iterator_t
{
    [NativeTypeName("xcb_bool32_t *")]
    public uint* data;

    public int rem;

    public int index;
}
