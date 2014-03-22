from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['/usr/lib/libid3tag.so'] = CDLL('/usr/lib/libid3tag.so')


ID3_TAG_RESTRICTION_TAGSIZE_64_FRAMES_128_KB = 64
ID3_FIELD_TYPE_LATIN1FULL = 2
ID3_FRAME_FLAG_GROUPINGIDENTITY = 64
ID3_FRAME_FLAG_ENCRYPTION = 4
def ID3_VERSION_STRINGIZE(str): return #str # macro
ID3_FIELD_TYPE_STRINGLIST = 6
ID3_TAG_OPTION_FILEALTERED = 32
ID3_TAG_RESTRICTION_TEXTENCODING_MASK = 32
ID3_FILE_MODE_READWRITE = 1
ID3_FILE_MODE_READONLY = 0
ID3_FIELD_TYPE_INT8 = 10
ID3_TAG_RESTRICTION_TEXTENCODING_LATIN1_UTF8 = 32
ID3_TAG_RESTRICTION_TAGSIZE_32_FRAMES_40_KB = 128
ID3_TAG_EXTENDEDFLAG_TAGISANUPDATE = 64
def ID3_VERSION_STRING(num): return ID3_VERSION_STRINGIZE(num) # macro
ID3_FRAME_FLAG_STATUSFLAGS = 65280
ID3_TAG_RESTRICTION_TAGSIZE_32_FRAMES_4_KB = 192
ID3_TAG_RESTRICTION_IMAGESIZE_NONE = 0
ID3_FRAME_FLAG_UNSYNCHRONISATION = 2
ID3_FRAME_FLAG_DATALENGTHINDICATOR = 1
ID3_TAG_RESTRICTION_TEXTENCODING_NONE = 0
ID3_FRAME_FLAG_READONLY = 4096
ID3_TAG_FLAG_KNOWNFLAGS = 240
ID3_TAG_RESTRICTION_TAGSIZE_MASK = 192
def ID3_TAG_VERSION_MAJOR(x): return (((x) >> 8) & 0xff) # macro
ID3_TAG_OPTION_UNSYNCHRONISATION = 1
ID3_TAG_RESTRICTION_IMAGESIZE_64_64_EXACT = 3
ID3_TAG_RESTRICTION_IMAGEENCODING_MASK = 4
ID3_TAG_RESTRICTION_IMAGESIZE_64_64 = 2
ID3_TAG_EXTENDEDFLAG_KNOWNFLAGS = 112
ID3_FIELD_TYPE_STRINGFULL = 5
ID3_TAG_RESTRICTION_IMAGESIZE_MASK = 3
ID3_TAG_RESTRICTION_TEXTSIZE_1024_CHARS = 8
ID3_TAG_RESTRICTION_TEXTSIZE_128_CHARS = 16
ID3_FIELD_TYPE_INT32PLUS = 14
ID3_TAG_RESTRICTION_TEXTSIZE_MASK = 24
ID3_FIELD_TYPE_BINARYDATA = 15
ID3_FIELD_TYPE_INT32 = 13
ID3_TAG_FLAG_FOOTERPRESENT = 16
ID3_FIELD_TYPE_INT16 = 11
def ID3_TAG_VERSION_MINOR(x): return (((x) >> 0) & 0xff) # macro
ID3_TAG_FLAG_EXTENDEDHEADER = 64
ID3_TAG_OPTION_APPENDEDTAG = 16
ID3_FIELD_TYPE_INT24 = 12
ID3_FIELD_TYPE_STRING = 4
ID3_FIELD_TYPE_LATIN1LIST = 3
ID3_TAG_FLAG_EXPERIMENTALINDICATOR = 32
ID3_FIELD_TYPE_LATIN1 = 1
ID3_TAG_EXTENDEDFLAG_TAGRESTRICTIONS = 16
ID3_FIELD_TYPE_TEXTENCODING = 0
ID3_TAG_FLAG_UNSYNCHRONISATION = 128
ID3_FRAME_FLAG_TAGALTERPRESERVATION = 16384
ID3_TAG_RESTRICTION_TEXTSIZE_30_CHARS = 24
ID3_TAG_RESTRICTION_IMAGESIZE_256_256 = 1
ID3_TAG_RESTRICTION_TAGSIZE_128_FRAMES_1_MB = 0
ID3_TAG_RESTRICTION_TEXTSIZE_NONE = 0
ID3_FRAME_FLAG_COMPRESSION = 8
ID3_TAG_OPTION_COMPRESSION = 2
ID3_FIELD_TYPE_DATE = 9
ID3_FRAME_FLAG_FORMATFLAGS = 255
ID3_FIELD_TYPE_LANGUAGE = 7
ID3_TAG_OPTION_ID3V1 = 256
ID3_TAG_EXTENDEDFLAG_CRCDATAPRESENT = 32
ID3_TAG_OPTION_CRC = 4
ID3_FRAME_FLAG_FILEALTERPRESERVATION = 8192
ID3_TAG_RESTRICTION_IMAGEENCODING_NONE = 0
ID3_FIELD_TEXTENCODING_UTF_8 = 3
ID3_FIELD_TEXTENCODING_UTF_16BE = 2
ID3_FIELD_TEXTENCODING_UTF_16 = 1
ID3_FRAME_FLAG_KNOWNFLAGS = 28751
ID3_FIELD_TYPE_FRAMEID = 8
ID3_FIELD_TEXTENCODING_ISO_8859_1 = 0
ID3_TAG_RESTRICTION_IMAGEENCODING_PNG_JPEG = 4
ID3_VERSION = '0.15.1 (beta)' # Variable STRING '(const char*)"0.15.1 (beta)"'
ID3_FRAME_TITLE = 'TIT2' # Variable STRING '(const char*)"TIT2"'
ID3_FRAME_OBSOLETE = 'ZOBS' # Variable STRING '(const char*)"ZOBS"'
ID3_PUBLISHYEAR = '2000-2004' # Variable STRING '(const char*)"2000-2004"'
ID3_FRAME_COMMENT = 'COMM' # Variable STRING '(const char*)"COMM"'
ID3_TAG_VERSION = 1024 # Variable c_int '1024'
ID3_AUTHOR = 'Underbit Technologies, Inc.' # Variable STRING '(const char*)"Underbit Technologies, Inc."'
ID3_FRAME_TRACK = 'TRCK' # Variable STRING '(const char*)"TRCK"'
ID3_FRAME_YEAR = 'TDRC' # Variable STRING '(const char*)"TDRC"'
ID3_VERSION_MINOR = 15 # Variable c_int '15'
ID3_VERSION_PATCH = 1 # Variable c_int '1'
ID3_FRAME_GENRE = 'TCON' # Variable STRING '(const char*)"TCON"'
ID3_VERSION_MAJOR = 0 # Variable c_int '0'
ID3_EMAIL = 'info@underbit.com' # Variable STRING '(const char*)"info@underbit.com"'
ID3_FRAME_ALBUM = 'TALB' # Variable STRING '(const char*)"TALB"'
ID3_TAG_QUERYSIZE = 10 # Variable c_int '10'
ID3_VERSION_EXTRA = ' (beta)' # Variable STRING '(const char*)" (beta)"'
__STDC_CONSTANT_MACROS = 1 # Variable c_int '1'
ID3_FRAME_ARTIST = 'TPE1' # Variable STRING '(const char*)"TPE1"'
id3_byte_t = c_ubyte
id3_length_t = c_ulong
id3_ucs4_t = c_ulong
id3_latin1_t = c_ubyte
id3_utf16_t = c_ushort
id3_utf8_t = c_byte
class id3_tag(Structure):
    pass
class id3_frame(Structure):
    pass
id3_tag._fields_ = [
    ('refcount', c_uint),
    ('version', c_uint),
    ('flags', c_int),
    ('extendedflags', c_int),
    ('restrictions', c_int),
    ('options', c_int),
    ('nframes', c_uint),
    ('frames', POINTER(POINTER(id3_frame))),
    ('paddedsize', id3_length_t),
]

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration
class id3_field(Union):
    pass
id3_frame._fields_ = [
    ('id', c_char * 5),
    ('description', STRING),
    ('refcount', c_uint),
    ('flags', c_int),
    ('group_id', c_int),
    ('encryption_method', c_int),
    ('encoded', POINTER(id3_byte_t)),
    ('encoded_length', id3_length_t),
    ('decoded_length', id3_length_t),
    ('nfields', c_uint),
    ('fields', POINTER(id3_field)),
]

# values for unnamed enumeration

# values for enumeration 'id3_field_type'
id3_field_type = c_int # enum

# values for enumeration 'id3_field_textencoding'
id3_field_textencoding = c_int # enum
class N9id3_field3DOT_9E(Structure):
    pass
N9id3_field3DOT_9E._fields_ = [
    ('type', id3_field_type),
    ('value', c_long),
]
class N9id3_field4DOT_10E(Structure):
    pass
N9id3_field4DOT_10E._fields_ = [
    ('type', id3_field_type),
    ('ptr', POINTER(id3_latin1_t)),
]
class N9id3_field4DOT_11E(Structure):
    pass
N9id3_field4DOT_11E._fields_ = [
    ('type', id3_field_type),
    ('nstrings', c_uint),
    ('strings', POINTER(POINTER(id3_latin1_t))),
]
class N9id3_field4DOT_12E(Structure):
    pass
N9id3_field4DOT_12E._fields_ = [
    ('type', id3_field_type),
    ('ptr', POINTER(id3_ucs4_t)),
]
class N9id3_field4DOT_13E(Structure):
    pass
N9id3_field4DOT_13E._fields_ = [
    ('type', id3_field_type),
    ('nstrings', c_uint),
    ('strings', POINTER(POINTER(id3_ucs4_t))),
]
class N9id3_field4DOT_14E(Structure):
    pass
N9id3_field4DOT_14E._fields_ = [
    ('type', id3_field_type),
    ('value', c_char * 9),
]
class N9id3_field4DOT_15E(Structure):
    pass
N9id3_field4DOT_15E._fields_ = [
    ('type', id3_field_type),
    ('data', POINTER(id3_byte_t)),
    ('length', id3_length_t),
]
id3_field._fields_ = [
    ('type', id3_field_type),
    ('number', N9id3_field3DOT_9E),
    ('latin1', N9id3_field4DOT_10E),
    ('latin1list', N9id3_field4DOT_11E),
    ('string', N9id3_field4DOT_12E),
    ('stringlist', N9id3_field4DOT_13E),
    ('immediate', N9id3_field4DOT_14E),
    ('binary', N9id3_field4DOT_15E),
]

# values for enumeration 'id3_file_mode'
id3_file_mode = c_int # enum
class id3_file(Structure):
    pass
id3_file._fields_ = [
]
id3_file_open = _libraries['/usr/lib/libid3tag.so'].id3_file_open
id3_file_open.restype = POINTER(id3_file)
id3_file_open.argtypes = [STRING, id3_file_mode]
id3_file_fdopen = _libraries['/usr/lib/libid3tag.so'].id3_file_fdopen
id3_file_fdopen.restype = POINTER(id3_file)
id3_file_fdopen.argtypes = [c_int, id3_file_mode]
id3_file_close = _libraries['/usr/lib/libid3tag.so'].id3_file_close
id3_file_close.restype = c_int
id3_file_close.argtypes = [POINTER(id3_file)]
id3_file_tag = _libraries['/usr/lib/libid3tag.so'].id3_file_tag
id3_file_tag.restype = POINTER(id3_tag)
id3_file_tag.argtypes = [POINTER(id3_file)]
id3_file_update = _libraries['/usr/lib/libid3tag.so'].id3_file_update
id3_file_update.restype = c_int
id3_file_update.argtypes = [POINTER(id3_file)]
id3_tag_new = _libraries['/usr/lib/libid3tag.so'].id3_tag_new
id3_tag_new.restype = POINTER(id3_tag)
id3_tag_new.argtypes = []
id3_tag_delete = _libraries['/usr/lib/libid3tag.so'].id3_tag_delete
id3_tag_delete.restype = None
id3_tag_delete.argtypes = [POINTER(id3_tag)]
id3_tag_version = _libraries['/usr/lib/libid3tag.so'].id3_tag_version
id3_tag_version.restype = c_uint
id3_tag_version.argtypes = [POINTER(id3_tag)]
id3_tag_options = _libraries['/usr/lib/libid3tag.so'].id3_tag_options
id3_tag_options.restype = c_int
id3_tag_options.argtypes = [POINTER(id3_tag), c_int, c_int]
id3_tag_setlength = _libraries['/usr/lib/libid3tag.so'].id3_tag_setlength
id3_tag_setlength.restype = None
id3_tag_setlength.argtypes = [POINTER(id3_tag), id3_length_t]
id3_tag_clearframes = _libraries['/usr/lib/libid3tag.so'].id3_tag_clearframes
id3_tag_clearframes.restype = None
id3_tag_clearframes.argtypes = [POINTER(id3_tag)]
id3_tag_attachframe = _libraries['/usr/lib/libid3tag.so'].id3_tag_attachframe
id3_tag_attachframe.restype = c_int
id3_tag_attachframe.argtypes = [POINTER(id3_tag), POINTER(id3_frame)]
id3_tag_detachframe = _libraries['/usr/lib/libid3tag.so'].id3_tag_detachframe
id3_tag_detachframe.restype = c_int
id3_tag_detachframe.argtypes = [POINTER(id3_tag), POINTER(id3_frame)]
id3_tag_findframe = _libraries['/usr/lib/libid3tag.so'].id3_tag_findframe
id3_tag_findframe.restype = POINTER(id3_frame)
id3_tag_findframe.argtypes = [POINTER(id3_tag), STRING, c_uint]
id3_tag_query = _libraries['/usr/lib/libid3tag.so'].id3_tag_query
id3_tag_query.restype = c_long
id3_tag_query.argtypes = [POINTER(id3_byte_t), id3_length_t]
id3_tag_parse = _libraries['/usr/lib/libid3tag.so'].id3_tag_parse
id3_tag_parse.restype = POINTER(id3_tag)
id3_tag_parse.argtypes = [POINTER(id3_byte_t), id3_length_t]
id3_tag_render = _libraries['/usr/lib/libid3tag.so'].id3_tag_render
id3_tag_render.restype = id3_length_t
id3_tag_render.argtypes = [POINTER(id3_tag), POINTER(id3_byte_t)]
id3_frame_new = _libraries['/usr/lib/libid3tag.so'].id3_frame_new
id3_frame_new.restype = POINTER(id3_frame)
id3_frame_new.argtypes = [STRING]
id3_frame_delete = _libraries['/usr/lib/libid3tag.so'].id3_frame_delete
id3_frame_delete.restype = None
id3_frame_delete.argtypes = [POINTER(id3_frame)]
id3_frame_field = _libraries['/usr/lib/libid3tag.so'].id3_frame_field
id3_frame_field.restype = POINTER(id3_field)
id3_frame_field.argtypes = [POINTER(id3_frame), c_uint]
id3_field_type = _libraries['/usr/lib/libid3tag.so'].id3_field_type
id3_field_type.restype = id3_field_type
id3_field_type.argtypes = [POINTER(id3_field)]
id3_field_setint = _libraries['/usr/lib/libid3tag.so'].id3_field_setint
id3_field_setint.restype = c_int
id3_field_setint.argtypes = [POINTER(id3_field), c_long]
id3_field_settextencoding = _libraries['/usr/lib/libid3tag.so'].id3_field_settextencoding
id3_field_settextencoding.restype = c_int
id3_field_settextencoding.argtypes = [POINTER(id3_field), id3_field_textencoding]
id3_field_setstrings = _libraries['/usr/lib/libid3tag.so'].id3_field_setstrings
id3_field_setstrings.restype = c_int
id3_field_setstrings.argtypes = [POINTER(id3_field), c_uint, POINTER(POINTER(id3_ucs4_t))]
id3_field_addstring = _libraries['/usr/lib/libid3tag.so'].id3_field_addstring
id3_field_addstring.restype = c_int
id3_field_addstring.argtypes = [POINTER(id3_field), POINTER(id3_ucs4_t)]
id3_field_setlanguage = _libraries['/usr/lib/libid3tag.so'].id3_field_setlanguage
id3_field_setlanguage.restype = c_int
id3_field_setlanguage.argtypes = [POINTER(id3_field), STRING]
id3_field_setlatin1 = _libraries['/usr/lib/libid3tag.so'].id3_field_setlatin1
id3_field_setlatin1.restype = c_int
id3_field_setlatin1.argtypes = [POINTER(id3_field), POINTER(id3_latin1_t)]
id3_field_setfulllatin1 = _libraries['/usr/lib/libid3tag.so'].id3_field_setfulllatin1
id3_field_setfulllatin1.restype = c_int
id3_field_setfulllatin1.argtypes = [POINTER(id3_field), POINTER(id3_latin1_t)]
id3_field_setstring = _libraries['/usr/lib/libid3tag.so'].id3_field_setstring
id3_field_setstring.restype = c_int
id3_field_setstring.argtypes = [POINTER(id3_field), POINTER(id3_ucs4_t)]
id3_field_setfullstring = _libraries['/usr/lib/libid3tag.so'].id3_field_setfullstring
id3_field_setfullstring.restype = c_int
id3_field_setfullstring.argtypes = [POINTER(id3_field), POINTER(id3_ucs4_t)]
id3_field_setframeid = _libraries['/usr/lib/libid3tag.so'].id3_field_setframeid
id3_field_setframeid.restype = c_int
id3_field_setframeid.argtypes = [POINTER(id3_field), STRING]
id3_field_setbinarydata = _libraries['/usr/lib/libid3tag.so'].id3_field_setbinarydata
id3_field_setbinarydata.restype = c_int
id3_field_setbinarydata.argtypes = [POINTER(id3_field), POINTER(id3_byte_t), id3_length_t]
id3_field_getint = _libraries['/usr/lib/libid3tag.so'].id3_field_getint
id3_field_getint.restype = c_long
id3_field_getint.argtypes = [POINTER(id3_field)]
id3_field_gettextencoding = _libraries['/usr/lib/libid3tag.so'].id3_field_gettextencoding
id3_field_gettextencoding.restype = id3_field_textencoding
id3_field_gettextencoding.argtypes = [POINTER(id3_field)]
id3_field_getlatin1 = _libraries['/usr/lib/libid3tag.so'].id3_field_getlatin1
id3_field_getlatin1.restype = POINTER(id3_latin1_t)
id3_field_getlatin1.argtypes = [POINTER(id3_field)]
id3_field_getfulllatin1 = _libraries['/usr/lib/libid3tag.so'].id3_field_getfulllatin1
id3_field_getfulllatin1.restype = POINTER(id3_latin1_t)
id3_field_getfulllatin1.argtypes = [POINTER(id3_field)]
id3_field_getstring = _libraries['/usr/lib/libid3tag.so'].id3_field_getstring
id3_field_getstring.restype = POINTER(id3_ucs4_t)
id3_field_getstring.argtypes = [POINTER(id3_field)]
id3_field_getfullstring = _libraries['/usr/lib/libid3tag.so'].id3_field_getfullstring
id3_field_getfullstring.restype = POINTER(id3_ucs4_t)
id3_field_getfullstring.argtypes = [POINTER(id3_field)]
id3_field_getnstrings = _libraries['/usr/lib/libid3tag.so'].id3_field_getnstrings
id3_field_getnstrings.restype = c_uint
id3_field_getnstrings.argtypes = [POINTER(id3_field)]
id3_field_getstrings = _libraries['/usr/lib/libid3tag.so'].id3_field_getstrings
id3_field_getstrings.restype = POINTER(id3_ucs4_t)
id3_field_getstrings.argtypes = [POINTER(id3_field), c_uint]
id3_field_getframeid = _libraries['/usr/lib/libid3tag.so'].id3_field_getframeid
id3_field_getframeid.restype = STRING
id3_field_getframeid.argtypes = [POINTER(id3_field)]
id3_field_getbinarydata = _libraries['/usr/lib/libid3tag.so'].id3_field_getbinarydata
id3_field_getbinarydata.restype = POINTER(id3_byte_t)
id3_field_getbinarydata.argtypes = [POINTER(id3_field), POINTER(id3_length_t)]
id3_genre_index = _libraries['/usr/lib/libid3tag.so'].id3_genre_index
id3_genre_index.restype = POINTER(id3_ucs4_t)
id3_genre_index.argtypes = [c_uint]
id3_genre_name = _libraries['/usr/lib/libid3tag.so'].id3_genre_name
id3_genre_name.restype = POINTER(id3_ucs4_t)
id3_genre_name.argtypes = [POINTER(id3_ucs4_t)]
id3_genre_number = _libraries['/usr/lib/libid3tag.so'].id3_genre_number
id3_genre_number.restype = c_int
id3_genre_number.argtypes = [POINTER(id3_ucs4_t)]
id3_ucs4_latin1duplicate = _libraries['/usr/lib/libid3tag.so'].id3_ucs4_latin1duplicate
id3_ucs4_latin1duplicate.restype = POINTER(id3_latin1_t)
id3_ucs4_latin1duplicate.argtypes = [POINTER(id3_ucs4_t)]
id3_ucs4_utf16duplicate = _libraries['/usr/lib/libid3tag.so'].id3_ucs4_utf16duplicate
id3_ucs4_utf16duplicate.restype = POINTER(id3_utf16_t)
id3_ucs4_utf16duplicate.argtypes = [POINTER(id3_ucs4_t)]
id3_ucs4_utf8duplicate = _libraries['/usr/lib/libid3tag.so'].id3_ucs4_utf8duplicate
id3_ucs4_utf8duplicate.restype = POINTER(id3_utf8_t)
id3_ucs4_utf8duplicate.argtypes = [POINTER(id3_ucs4_t)]
id3_ucs4_putnumber = _libraries['/usr/lib/libid3tag.so'].id3_ucs4_putnumber
id3_ucs4_putnumber.restype = None
id3_ucs4_putnumber.argtypes = [POINTER(id3_ucs4_t), c_ulong]
id3_ucs4_getnumber = _libraries['/usr/lib/libid3tag.so'].id3_ucs4_getnumber
id3_ucs4_getnumber.restype = c_ulong
id3_ucs4_getnumber.argtypes = [POINTER(id3_ucs4_t)]
id3_latin1_ucs4duplicate = _libraries['/usr/lib/libid3tag.so'].id3_latin1_ucs4duplicate
id3_latin1_ucs4duplicate.restype = POINTER(id3_ucs4_t)
id3_latin1_ucs4duplicate.argtypes = [POINTER(id3_latin1_t)]
id3_utf16_ucs4duplicate = _libraries['/usr/lib/libid3tag.so'].id3_utf16_ucs4duplicate
id3_utf16_ucs4duplicate.restype = POINTER(id3_ucs4_t)
id3_utf16_ucs4duplicate.argtypes = [POINTER(id3_utf16_t)]
id3_utf8_ucs4duplicate = _libraries['/usr/lib/libid3tag.so'].id3_utf8_ucs4duplicate
id3_utf8_ucs4duplicate.restype = POINTER(id3_ucs4_t)
id3_utf8_ucs4duplicate.argtypes = [POINTER(id3_utf8_t)]
id3_version = (c_char * 0).in_dll(_libraries['/usr/lib/libid3tag.so'], 'id3_version')
id3_copyright = (c_char * 0).in_dll(_libraries['/usr/lib/libid3tag.so'], 'id3_copyright')
id3_author = (c_char * 0).in_dll(_libraries['/usr/lib/libid3tag.so'], 'id3_author')
id3_build = (c_char * 0).in_dll(_libraries['/usr/lib/libid3tag.so'], 'id3_build')
__all__ = ['ID3_FRAME_FLAG_UNSYNCHRONISATION',
           'id3_field_getfulllatin1',
           'ID3_TAG_EXTENDEDFLAG_KNOWNFLAGS', 'id3_build',
           'ID3_FRAME_TRACK', 'id3_field_gettextencoding',
           'ID3_FIELD_TYPE_STRINGLIST', 'id3_tag_findframe',
           'id3_latin1_ucs4duplicate', 'ID3_FILE_MODE_READWRITE',
           'ID3_FIELD_TYPE_INT8', 'ID3_FIELD_TYPE_LANGUAGE',
           'ID3_TAG_OPTION_ID3V1',
           'ID3_TAG_RESTRICTION_TAGSIZE_32_FRAMES_4_KB',
           'ID3_TAG_RESTRICTION_TEXTENCODING_NONE',
           'ID3_TAG_FLAG_KNOWNFLAGS',
           'ID3_FIELD_TEXTENCODING_ISO_8859_1', 'ID3_VERSION_STRING',
           'ID3_FIELD_TYPE_STRING', 'ID3_FIELD_TEXTENCODING_UTF_16BE',
           'id3_frame_field', 'ID3_FRAME_FLAG_KNOWNFLAGS',
           'ID3_TAG_RESTRICTION_TEXTSIZE_1024_CHARS',
           'id3_field_addstring', 'id3_field_getframeid',
           'id3_utf8_ucs4duplicate', 'N9id3_field4DOT_10E',
           'ID3_VERSION_MINOR', 'ID3_FIELD_TYPE_INT32PLUS',
           'ID3_TAG_RESTRICTION_TEXTENCODING_MASK',
           'ID3_FRAME_FLAG_ENCRYPTION', 'id3_frame_new',
           'id3_tag_clearframes',
           'ID3_TAG_EXTENDEDFLAG_TAGISANUPDATE',
           'ID3_TAG_RESTRICTION_IMAGESIZE_64_64',
           'id3_tag_attachframe', 'ID3_FRAME_YEAR',
           'ID3_FIELD_TEXTENCODING_UTF_8',
           'ID3_TAG_RESTRICTION_IMAGESIZE_256_256',
           'id3_field_getstring', 'ID3_EMAIL', 'ID3_FRAME_ALBUM',
           'id3_tag_render', 'N9id3_field4DOT_12E', 'id3_tag_delete',
           'ID3_TAG_FLAG_EXTENDEDHEADER', 'id3_utf16_t',
           'ID3_TAG_RESTRICTION_IMAGEENCODING_MASK',
           'ID3_TAG_FLAG_EXPERIMENTALINDICATOR',
           'id3_field_textencoding', 'id3_field_setbinarydata',
           'ID3_TAG_QUERYSIZE', 'id3_file_tag', 'id3_author',
           'id3_file_open', 'id3_field_setfullstring',
           'id3_field_setframeid', 'id3_tag_setlength',
           'ID3_TAG_RESTRICTION_IMAGESIZE_NONE', 'ID3_TAG_VERSION',
           'ID3_TAG_OPTION_APPENDEDTAG', 'id3_field_setlatin1',
           'ID3_FIELD_TYPE_BINARYDATA',
           'ID3_FRAME_FLAG_DATALENGTHINDICATOR', 'id3_ucs4_t',
           'ID3_TAG_RESTRICTION_IMAGEENCODING_PNG_JPEG',
           'id3_field_setlanguage', 'id3_field_getstrings',
           'id3_field_setint',
           'ID3_TAG_RESTRICTION_TAGSIZE_128_FRAMES_1_MB',
           'ID3_TAG_FLAG_UNSYNCHRONISATION', 'id3_ucs4_getnumber',
           'ID3_FIELD_TYPE_INT16', 'id3_file',
           'id3_field_setfulllatin1', 'ID3_FIELD_TYPE_TEXTENCODING',
           'ID3_VERSION', 'id3_ucs4_latin1duplicate',
           'ID3_TAG_RESTRICTION_TAGSIZE_64_FRAMES_128_KB',
           'id3_field_settextencoding', 'id3_tag_options',
           'N9id3_field4DOT_14E', 'id3_field_setstring',
           'id3_tag_new', 'ID3_FIELD_TYPE_FRAMEID',
           'id3_field_getlatin1', 'id3_field_getbinarydata',
           'ID3_TAG_RESTRICTION_TEXTSIZE_NONE',
           'ID3_TAG_RESTRICTION_TEXTENCODING_LATIN1_UTF8',
           'id3_field_setstrings',
           'ID3_TAG_RESTRICTION_IMAGESIZE_MASK', 'id3_genre_name',
           'id3_field_getnstrings',
           'ID3_TAG_OPTION_UNSYNCHRONISATION',
           'ID3_FRAME_FLAG_GROUPINGIDENTITY', 'ID3_FIELD_TYPE_INT24',
           'id3_byte_t', 'ID3_FIELD_TEXTENCODING_UTF_16',
           'ID3_TAG_RESTRICTION_TAGSIZE_32_FRAMES_40_KB', 'id3_field',
           'ID3_TAG_OPTION_CRC', 'ID3_PUBLISHYEAR',
           'ID3_FRAME_FLAG_COMPRESSION', 'id3_tag_version',
           'ID3_VERSION_STRINGIZE', 'N9id3_field4DOT_15E',
           'id3_file_mode', 'id3_length_t',
           'ID3_FRAME_FLAG_STATUSFLAGS', 'ID3_FIELD_TYPE_LATIN1FULL',
           'ID3_TAG_RESTRICTION_TEXTSIZE_30_CHARS',
           'ID3_FIELD_TYPE_LATIN1LIST', 'ID3_FILE_MODE_READONLY',
           'ID3_TAG_EXTENDEDFLAG_CRCDATAPRESENT', 'id3_field_type',
           'id3_utf8_t', 'id3_file_fdopen',
           'ID3_FIELD_TYPE_STRINGFULL', 'ID3_FRAME_ARTIST',
           'ID3_FIELD_TYPE_INT32', 'ID3_FRAME_FLAG_READONLY',
           'ID3_TAG_RESTRICTION_TEXTSIZE_128_CHARS',
           'N9id3_field4DOT_13E', 'ID3_FIELD_TYPE_DATE',
           'id3_latin1_t', 'id3_file_close', 'N9id3_field3DOT_9E',
           '__STDC_CONSTANT_MACROS', 'id3_tag',
           'id3_ucs4_utf16duplicate', 'id3_copyright',
           'id3_field_getint', 'N9id3_field4DOT_11E',
           'ID3_FRAME_FLAG_FORMATFLAGS', 'ID3_FRAME_GENRE',
           'ID3_FRAME_FLAG_TAGALTERPRESERVATION',
           'ID3_TAG_VERSION_MAJOR', 'id3_genre_number',
           'ID3_FIELD_TYPE_LATIN1', 'id3_version',
           'ID3_TAG_OPTION_FILEALTERED',
           'ID3_FRAME_FLAG_FILEALTERPRESERVATION',
           'ID3_TAG_RESTRICTION_IMAGESIZE_64_64_EXACT',
           'ID3_FRAME_COMMENT', 'id3_genre_index', 'ID3_AUTHOR',
           'id3_field_getfullstring', 'id3_file_update',
           'ID3_TAG_EXTENDEDFLAG_TAGRESTRICTIONS',
           'ID3_TAG_OPTION_COMPRESSION',
           'ID3_TAG_RESTRICTION_TEXTSIZE_MASK',
           'id3_utf16_ucs4duplicate', 'ID3_VERSION_EXTRA',
           'ID3_TAG_RESTRICTION_IMAGEENCODING_NONE',
           'id3_ucs4_putnumber', 'ID3_FRAME_TITLE',
           'ID3_FRAME_OBSOLETE', 'id3_ucs4_utf8duplicate',
           'id3_tag_query', 'ID3_TAG_VERSION_MINOR',
           'id3_tag_detachframe', 'ID3_VERSION_PATCH',
           'id3_frame_delete', 'ID3_VERSION_MAJOR', 'id3_frame',
           'id3_tag_parse', 'ID3_TAG_RESTRICTION_TAGSIZE_MASK',
           'ID3_TAG_FLAG_FOOTERPRESENT']
