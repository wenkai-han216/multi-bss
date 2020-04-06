APPNAME = 'ns'
AR = ['/usr/bin/ar']
ARFLAGS = ['rcs']
BINDIR = '/usr/local/bin'
BUILD_PROFILE = 'optimized'
BUILD_SUFFIX = '-optimized'
CC = ['/usr/bin/gcc']
CCDEFINES = []
CCFLAGS = ['-O3', '-g', '-Wall', '-Werror', '-O3', '-g', '-Wall', '-Werror', '-march=native', '-fstrict-overflow', '-Wstrict-overflow=2', '-std=c++11', '-fstrict-aliasing', '-Wstrict-aliasing']
CCFLAGS_PTHREAD = '-pthread'
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('5', '4', '0')
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_PYEMBED = ['-fno-strict-aliasing', '-g', '-fwrapv', '-O2', '-g', '-fstack-protector-strong', '-fno-strict-aliasing']
CFLAGS_PYEXT = ['-pthread', '-fno-strict-aliasing', '-g', '-fwrapv', '-O2', '-g', '-fstack-protector-strong', '-fno-strict-aliasing', '-g', '-fwrapv', '-O2', '-g', '-fstack-protector-strong', '-fno-strict-aliasing']
CFLAGS_cshlib = ['-fPIC']
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXDEFINES = []
CXXFLAGS = ['-O3', '-g', '-Wall', '-Werror', '-march=native', '-fstrict-overflow', '-Wstrict-overflow=2', '-std=c++11', '-fstrict-aliasing', '-Wstrict-aliasing']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_PTHREAD = '-pthread'
CXXFLAGS_PYEMBED = ['-fno-strict-aliasing', '-g', '-fwrapv', '-O2', '-g', '-fstack-protector-strong', '-fno-strict-aliasing']
CXXFLAGS_PYEXT = ['-pthread', '-fno-strict-aliasing', '-g', '-fwrapv', '-O2', '-g', '-fstack-protector-strong', '-fno-strict-aliasing', '-g', '-fwrapv', '-O2', '-g', '-fstack-protector-strong', '-fno-strict-aliasing']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DATADIR = '/usr/local/share'
DATAROOTDIR = '/usr/local/share'
DEFINES = ['NS3_BUILD_PROFILE_OPTIMIZED', 'HAVE_SYS_IOCTL_H=1', 'HAVE_IF_NETS_H=1', 'HAVE_NET_ETHERNET_H=1', 'HAVE_PACKET_H=1', 'HAVE_IF_TUN_H=1']
DEFINES_PYEMBED = ['NDEBUG', '_FORTIFY_SOURCE=2']
DEFINES_PYEXT = ['NDEBUG', '_FORTIFY_SOURCE=2', 'NDEBUG', '_FORTIFY_SOURCE=2']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'HAVE_SYS_IOCTL_H': '', 'HAVE_IF_NETS_H': '', 'HAVE_SIGNAL_H': '', 'HAVE_SYS_TYPES_H': '', 'PYTHONDIR': '', 'INT64X64_USE_128': '', 'HAVE_PACKET_H': '', 'HAVE_STDINT_H': '', 'HAVE_NET_ETHERNET_H': '', 'HAVE_SYS_STAT_H': '', 'HAVE_DIRENT_H': '', 'HAVE_INTTYPES_H': '', 'HAVE_STDLIB_H': '', 'HAVE_PTHREAD_H': '', 'HAVE_PYTHON_H': '', 'HAVE___UINT128_T': '', 'PYTHONARCHDIR': '', 'HAVE_GETENV': '', 'HAVE_RT': '', 'HAVE_IF_TUN_H': '', 'HAVE_SYS_INT_TYPES_H': '', 'HAVE_UINT128_T': ''}
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
DOCDIR = '/usr/local/share/doc/ns'
DVIDIR = '/usr/local/share/doc/ns'
ENABLE_BRITE = False
ENABLE_EMU = True
ENABLE_EXAMPLES = True
ENABLE_FDNETDEV = True
ENABLE_GSL = None
ENABLE_GTK = None
ENABLE_LIBXML2 = None
ENABLE_NSC = False
ENABLE_PYTHON_BINDINGS = False
ENABLE_PYVIZ = False
ENABLE_REAL_TIME = True
ENABLE_STATIC_NS3 = False
ENABLE_SUDO = False
ENABLE_TAP = True
ENABLE_TESTS = True
ENABLE_THREADING = True
EXAMPLE_DIRECTORIES = ['udp-client-server', 'stats', 'energy', 'tcp', 'routing', 'traffic-control', 'tutorial', 'ipv6', 'wireless', 'realtime', 'socket', 'error-model', 'naming', 'udp', 'matrix-topology']
EXEC_PREFIX = '/usr/local'
HAVE_DIRENT_H = 1
HAVE_INTTYPES_H = 1
HAVE_LINUX_IF_TUN_H = 1
HAVE_NETPACKET_PACKET_H = 1
HAVE_NET_ETHERNET_H = 1
HAVE_NET_IF_H = 1
HAVE_PTHREAD_H = 1
HAVE_RT = 1
HAVE_SIGNAL_H = 1
HAVE_STDINT_H = 1
HAVE_STDLIB_H = 1
HAVE_SYS_IOCTL_H = 1
HAVE_SYS_STAT_H = 1
HAVE_SYS_TYPES_H = 1
HAVE___UINT128_T = 1
HTMLDIR = '/usr/local/share/doc/ns'
INCLUDEDIR = '/usr/local/include'
INCLUDES_PYEMBED = ['/usr/include/python2.7']
INCLUDES_PYEXT = ['/usr/include/python2.7']
INFODIR = '/usr/local/share/info'
INT64X64_USE_128 = 1
LIBDIR = '/usr/local/lib'
LIBEXECDIR = '/usr/local/libexec'
LIBPATH_PYEMBED = ['/usr/lib/python2.7/config-x86_64-linux-gnu']
LIBPATH_PYEXT = ['/usr/lib/python2.7/config-x86_64-linux-gnu']
LIBPATH_PYTHON2.7 = ['/usr/lib/python2.7/config-x86_64-linux-gnu']
LIBPATH_ST = '-L%s'
LIB_BOOST = []
LIB_PYEMBED = ['python2.7']
LIB_PYEXT = ['python2.7']
LIB_PYTHON2.7 = ['python2.7']
LIB_RT = ['rt']
LIB_ST = '-l%s'
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_PTHREAD = '-pthread'
LINKFLAGS_PYEMBED = ['-Wl,-Bsymbolic-functions', '-Wl,-z,relro']
LINKFLAGS_PYEXT = ['-Wl,-Bsymbolic-functions', '-Wl,-z,relro', '-pthread', '-Wl,-O1', '-Wl,-Bsymbolic-functions', '-Wl,-Bsymbolic-functions', '-Wl,-z,relro']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/usr/bin/gcc']
LINK_CXX = ['/usr/bin/g++']
LOCALEDIR = '/usr/local/share/locale'
LOCALSTATEDIR = '/usr/local/var'
MANDIR = '/usr/local/share/man'
MODULES_NOT_BUILT = ['brite', 'click', 'openflow', 'visualizer']
NS3_CONTRIBUTED_MODULES = []
NS3_ENABLED_CONTRIBUTED_MODULES = []
NS3_ENABLED_MODULES = ['ns3-antenna', 'ns3-aodv', 'ns3-applications', 'ns3-bridge', 'ns3-buildings', 'ns3-config-store', 'ns3-core', 'ns3-csma', 'ns3-csma-layout', 'ns3-dsdv', 'ns3-dsr', 'ns3-energy', 'ns3-fd-net-device', 'ns3-flow-monitor', 'ns3-internet', 'ns3-internet-apps', 'ns3-lr-wpan', 'ns3-lte', 'ns3-lte-wifi-coexistence', 'ns3-mesh', 'ns3-mobility', 'ns3-mpi', 'ns3-netanim', 'ns3-network', 'ns3-nix-vector-routing', 'ns3-olsr', 'ns3-point-to-point', 'ns3-point-to-point-layout', 'ns3-propagation', 'ns3-sixlowpan', 'ns3-spectrum', 'ns3-stats', 'ns3-tap-bridge', 'ns3-test', 'ns3-topology-read', 'ns3-traffic-control', 'ns3-uan', 'ns3-virtual-net-device', 'ns3-wave', 'ns3-wifi', 'ns3-wifi-he', 'ns3-wimax']
NS3_EXECUTABLE_PATH = ['/home/wenkaihan/mbss/ns-3-dev-11ax/build/src/fd-net-device', '/home/wenkaihan/mbss/ns-3-dev-11ax/build/src/tap-bridge']
NS3_MODULES = ['ns3-antenna', 'ns3-aodv', 'ns3-applications', 'ns3-bridge', 'ns3-buildings', 'ns3-config-store', 'ns3-core', 'ns3-csma', 'ns3-csma-layout', 'ns3-dsdv', 'ns3-dsr', 'ns3-energy', 'ns3-fd-net-device', 'ns3-flow-monitor', 'ns3-internet', 'ns3-internet-apps', 'ns3-lr-wpan', 'ns3-lte', 'ns3-lte-wifi-coexistence', 'ns3-mesh', 'ns3-mobility', 'ns3-mpi', 'ns3-netanim', 'ns3-network', 'ns3-nix-vector-routing', 'ns3-olsr', 'ns3-point-to-point', 'ns3-point-to-point-layout', 'ns3-propagation', 'ns3-sixlowpan', 'ns3-spectrum', 'ns3-stats', 'ns3-tap-bridge', 'ns3-test', 'ns3-topology-read', 'ns3-traffic-control', 'ns3-uan', 'ns3-virtual-net-device', 'ns3-wave', 'ns3-wifi', 'ns3-wifi-he', 'ns3-wimax']
NS3_MODULE_PATH = ['/usr/lib/gcc/x86_64-linux-gnu/5', '/home/wenkaihan/mbss/ns-3-dev-11ax/build/lib']
NS3_OPTIONAL_FEATURES = [('python', 'Python Bindings', False, 'Python library or headers missing'), ('brite', 'BRITE Integration', False, 'BRITE not enabled (see option --with-brite)'), ('nsclick', 'NS-3 Click Integration', False, 'nsclick not enabled (see option --with-nsclick)'), ('GtkConfigStore', 'GtkConfigStore', [], "library 'gtk+-3.0 >= 3.0' not found"), ('XmlIo', 'XmlIo', [], "library 'libxml-2.0 >= 2.7' not found"), ('Threading', 'Threading Primitives', True, '<pthread.h> include not detected'), ('RealTime', 'Real Time Simulator', True, 'threading not enabled'), ('FdNetDevice', 'File descriptor NetDevice', True, 'FdNetDevice module enabled'), ('TapFdNetDevice', 'Tap FdNetDevice', True, 'Tap support enabled'), ('EmuFdNetDevice', 'Emulation FdNetDevice', True, 'Emulation support enabled'), ('PlanetLabFdNetDevice', 'PlanetLab FdNetDevice', False, 'PlanetLab operating system not detected (see option --force-planetlab)'), ('nsc', 'Network Simulation Cradle', False, 'NSC not found (see option --with-nsc)'), ('mpi', 'MPI Support', False, 'option --enable-mpi not selected'), ('openflow', 'NS-3 OpenFlow Integration', False, 'Required boost libraries not found'), ('SqliteDataOutput', 'SQlite stats data output', [], "library 'sqlite3' not found"), ('TapBridge', 'Tap Bridge', True, '<linux/if_tun.h> include not detected'), ('PyViz', 'PyViz visualizer', False, 'Python Bindings are needed but not enabled'), ('ENABLE_SUDO', 'Use sudo to set suid bit', False, 'option --enable-sudo not selected'), ('ENABLE_TESTS', 'Tests', True, 'option --enable-tests selected'), ('ENABLE_EXAMPLES', 'Examples', True, 'option --enable-examples selected'), ('GSL', 'GNU Scientific Library (GSL)', [], 'GSL not found'), ('libgcrypt', 'Gcrypt library', [], 'libgcrypt not found: you can use libgcrypt-config to find its location.'), ('DES Metrics', 'DES Metrics event collection', [], 'defaults to disabled')]
OLDINCLUDEDIR = '/usr/include'
PACKAGE = 'ns'
PDFDIR = '/usr/local/share/doc/ns'
PKGCONFIG = ['/usr/bin/pkg-config']
PLATFORM = 'linux2'
PREFIX = '/usr/local'
PRINT_BUILT_MODULES_AT_END = False
PSDIR = '/usr/local/share/doc/ns'
PYC = 1
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTHON = ['/usr/bin/python']
PYTHONARCHDIR = '/usr/local/lib/python2.7/dist-packages'
PYTHONDIR = '/usr/local/lib/python2.7/dist-packages'
PYTHON_VERSION = '2.7'
REQUIRED_BOOST_LIBS = ['system', 'signals', 'filesystem']
RPATH_ST = '-Wl,-rpath,%s'
SBINDIR = '/usr/local/sbin'
SHAREDSTATEDIR = '/usr/local/com'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
SQLITE_STATS = None
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SUDO = ['/usr/bin/sudo']
SYSCONFDIR = '/usr/local/etc'
VALGRIND_FOUND = False
VERSION = '3-dev'
WL_SONAME_SUPPORTED = True
cfg_files = ['/home/wenkaihan/mbss/ns-3-dev-11ax/build/ns3/config-store-config.h', '/home/wenkaihan/mbss/ns-3-dev-11ax/build/ns3/core-config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_SYS_IOCTL_H', 'HAVE_IF_NETS_H', 'HAVE_NET_ETHERNET_H', 'HAVE_IF_TUN_H', 'HAVE_PACKET_H']
macbundle_PATTERN = '%s.bundle'
pyext_PATTERN = '%s.so'
