namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_ungrab_keyboard_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("xcb_timestamp_t")]
    public uint time;
}
