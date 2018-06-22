{
  'targets': [
    {
      'target_name': 'physx-node',
      'conditions': [
        ['OS=="win"', {
          'sources': [
            'main.cpp',
            'deps/PxShared/src/foundation/src/*.cpp',
            'deps/PxShared/src/foundation/src/windows/*.cpp',
          ],
          'include_dirs': [
            'deps/PxShared/include',
            'deps/PxShared/src/foundation/include',
            'deps/PxShared/src/foundation/include/windows',
          ],
          'library_dirs': [
          ],
          'libraries': [
          ],
          'copies': [
          ],
          'defines': [
            'NDEBUG',
            'WIN32',
            '_CRT_SECURE_NO_DEPRECATE',
            '_CRT_NONSTDC_NO_DEPRECATE',
            '_WINSOCK_DEPRECATED_NO_WARNINGS',
            'DISABLE_CUDA_PHYSX',
            'PX_FOUNDATION_DLL=1',
          ],
        }],
        ['OS=="win"', {
          'sources': [
            'deps/PhysX_3.4/Source/Common/src/*.cpp',
            'deps/PhysX_3.4/Source/Common/src/windows/*.cpp',
          ],
          'include_dirs': [
            'deps/PhysX_3.4/Source/Common/include',
            'deps/PhysX_3.4/Source/Common/include/windows',
            'deps/PhysX_3.4/Include/Common',
            'deps/PhysX_3.4/Include/Common/windows',
            'deps/PhysX_3.4/Include',
            'deps/PhysX_3.4/Source/GeomUtils/headers',
          ],
          'library_dirs': [
          ],
          'libraries': [
          ],
          'copies': [
          ],
          'defines': [
          'NDEBUG',
          'WIN32',
          '_CRT_SECURE_NO_DEPRECATE',
          '_CRT_NONSTDC_NO_DEPRECATE',
          '_WINSOCK_DEPRECATED_NO_WARNINGS',
          'PX_FOUNDATION_DLL=1',
          'PX_PHYSX_COMMON_EXPORTS',
          ],
        }],
        ['OS=="linux"', {
          'sources': [
            'main.cpp',
          ],
          'include_dirs': [
          ],
          'library_dirs': [
          ],
          'libraries': [
          ],
          'copies': [
          ],
          'defines': [
          ],
        }],
        ['OS=="mac"', {
          'sources': [
            'main.cpp',
          ],
          'include_dirs': [
          ],
          'library_dirs': [
          ],
          'libraries': [
          ],
          'copies': [
          ],
          'defines': [
          ],
        }],
      ],
    },
  ],
}
