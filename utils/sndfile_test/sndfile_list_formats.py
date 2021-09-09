import sndfile

info = sndfile.SF_FORMAT_INFO()
sfinfo = sndfile.SF_INFO()
iformat = sndfile.c_int()
major_count = sndfile.c_int()
subtype_count = sndfile.c_int()
sndfile.sf_command(
    None,
    sndfile.SFC_GET_FORMAT_MAJOR_COUNT,
    sndfile.byref(major_count),
    sndfile.sizeof(sndfile.c_int)
)
sndfile.sf_command(
    None,
    sndfile.SFC_GET_FORMAT_SUBTYPE_COUNT,
    sndfile.byref(subtype_count),
    sndfile.sizeof(sndfile.c_int)
)

sfinfo.channels = 1
for m in range(major_count.value):
    info.format = m
    sndfile.sf_command(
        None,
        sndfile.SFC_GET_FORMAT_MAJOR,
        sndfile.byref(info),
        sndfile.sizeof(info)
    )
    print(f"{info.name} (extension \"{info.extension}\")")
    iformat = info.format
    for s in range(subtype_count.value):
        info.format = s
        sndfile.sf_command(
            None,
            sndfile.SFC_GET_FORMAT_SUBTYPE,
            sndfile.byref(info),
            sndfile.sizeof(info)
        )

        iformat = (iformat & sndfile.SF_FORMAT_TYPEMASK) | info.format
        sfinfo.format = iformat
        if sndfile.sf_format_check(sfinfo):
            print(f"   {info.name}")
    print()
