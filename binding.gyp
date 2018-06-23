{
  'targets': [
    {
      'target_name': 'physx',
      'include_dirs': ["<!(node -e \"require('nan')\")"],
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
            'deps/PhysX_3.4/Source/GeomUtils/src/*.cpp',
            'deps/PhysX_3.4/Source/GeomUtils/src/ccd/*.cpp',
            'deps/PhysX_3.4/Source/GeomUtils/src/common/*.cpp',
            'deps/PhysX_3.4/Source/GeomUtils/src/contact/*.cpp',
            'deps/PhysX_3.4/Source/GeomUtils/src/convex/*.cpp',
            'deps/PhysX_3.4/Source/GeomUtils/src/distance/*.cpp',
            'deps/PhysX_3.4/Source/GeomUtils/src/gjk/*.cpp',
            'deps/PhysX_3.4/Source/GeomUtils/src/hf/*.cpp',
            'deps/PhysX_3.4/Source/GeomUtils/src/intersection/*.cpp',
            'deps/PhysX_3.4/Source/GeomUtils/src/mesh/*.cpp',
            'deps/PhysX_3.4/Source/GeomUtils/src/pcm/*.cpp',
            'deps/PhysX_3.4/Source/GeomUtils/src/sweep/*.cpp',
          ],
          'include_dirs': [
            'deps/PhysX_3.4/Source/Common/src',
            'deps/PhysX_3.4/Source/Common/include',
            'deps/PhysX_3.4/Source/Common/include/windows',
            'deps/PhysX_3.4/Include/Common',
            'deps/PhysX_3.4/Include/Common/windows',
            'deps/PhysX_3.4/Include',
            'deps/PhysX_3.4/Include/GeomUtils',
            'deps/PhysX_3.4/Source/GeomUtils/headers',
            'deps/PhysX_3.4/Source/GeomUtils/src',
            'deps/PhysX_3.4/Source/GeomUtils/src/ccd',
            'deps/PhysX_3.4/Source/GeomUtils/src/common',
            'deps/PhysX_3.4/Source/GeomUtils/src/contact',
            'deps/PhysX_3.4/Source/GeomUtils/src/convex',
            'deps/PhysX_3.4/Source/GeomUtils/src/distance',
            'deps/PhysX_3.4/Source/GeomUtils/src/gjk',
            'deps/PhysX_3.4/Source/GeomUtils/src/hf',
            'deps/PhysX_3.4/Source/GeomUtils/src/intersection',
            'deps/PhysX_3.4/Source/GeomUtils/src/mesh',
            'deps/PhysX_3.4/Source/GeomUtils/src/pcm',
            'deps/PhysX_3.4/Source/GeomUtils/src/sweep',
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
        ['OS=="win"', {
          'sources': [
            'deps/PhysX_3.4/Source/PhysX/src/*.cpp',
            'deps/PhysX_3.4/Source/PhysX/src/windows/*.cpp',
            'deps/PhysX_3.4/Source/PhysX/src/buffering/*.cpp',
            'deps/PhysX_3.4/Source/PhysX/src/cloth/*.cpp',
            'deps/PhysX_3.4/Source/PhysX/src/particles/*.cpp',
            'deps/PhysX_3.4/Source/SimulationController/src/*.cpp',
            'deps/PxShared/src/task/src/*.cpp',
            'deps/PhysX_3.4/Source/LowLevel/API/src/*.cpp',
            'deps/PhysX_3.4/Source/LowLevel/common/src/collision/*.cpp',
            'deps/PhysX_3.4/Source/LowLevel/common/src/pipeline/*.cpp',
            'deps/PhysX_3.4/Source/LowLevel/software/src/*.cpp',
            'deps/PhysX_3.4/Source/LowLevelAABB/src/*.cpp',
            'deps/PhysX_3.4/Source/LowLevelCloth/src/*.cpp',
            'deps/PhysX_3.4/Source/LowLevelCloth/src/avx/*.cpp',
            'deps/PhysX_3.4/Source/LowLevelDynamics/src/*.cpp',
            'deps/PhysX_3.4/Source/LowLevelParticles/src/*.cpp',
            'deps/PhysX_3.4/Source/SceneQuery/src/*.cpp',
            'deps/PhysX_3.4/Source/SimulationController/src/*.cpp',
            'deps/PhysX_3.4/Source/SimulationController/src/cloth/*.cpp',
            'deps/PhysX_3.4/Source/SimulationController/src/particles/*.cpp',
          ],
          'include_dirs': [
            'deps/PhysX_3.4/Source/PhysX/include',
            'deps/PhysX_3.4/Source/PhysX/include/windows',
            'deps/PhysX_3.4/Include/PhysX',
            'deps/PhysX_3.4/Include/PhysX/windows',
            'deps/PhysX_3.4/Source/PhysX/src',
            'deps/PhysX_3.4/Source/PhysX/src/buffering',
            'deps/PhysX_3.4/Source/PhysX/src/cloth',
            'deps/PhysX_3.4/Source/PhysX/src/particles',
            'deps/PhysX_3.4/Include/particles',
            'deps/PhysX_3.4/Source/SimulationController/include',
            'deps/PxShared/src/pvd/include',
            'deps/PxShared/include',
            'deps/PhysX_3.4/Source/LowLevel/API/include',
            'deps/PhysX_3.4/Source/LowLevel/common/include/collision',
            'deps/PhysX_3.4/Source/LowLevel/common/include/pipeline',
            'deps/PhysX_3.4/Source/LowLevel/common/include/utils',
            'deps/PhysX_3.4/Source/LowLevel/software/include',
            'deps/PhysX_3.4/Source/LowLevelAABB/include',
            'deps/PhysX_3.4/Source/LowLevelCloth/include',
            'deps/PhysX_3.4/Source/LowLevelCloth/src/avx',
            'deps/PhysX_3.4/Source/LowLevelCloth/src/sse',
            'deps/PhysX_3.4/Source/LowLevelDynamics/include',
            'deps/PhysX_3.4/Source/LowLevelParticles/include',
            'deps/PhysX_3.4/Include/geometry',
            'deps/PhysX_3.4/Source/SceneQuery/src',
            'deps/PhysX_3.4/Source/SceneQuery/include',
            'deps/PhysX_3.4/Include/cloth',
            'deps/PhysX_3.4/Include/extensions',
            'deps/PhysX_3.4/Source/SimulationController/include',
            'deps/PhysX_3.4/Source/SimulationController/src',
            'deps/PhysX_3.4/Source/SimulationController/src/cloth',
            'deps/PhysX_3.4/Source/SimulationController/src/particles',
          ],
          'library_dirs': [
          ],
          'libraries': [
          ],
          'copies': [
          ],
          'defines': [
            'WIN32',
            '_CRT_SECURE_NO_DEPRECATE',
            '_CRT_NONSTDC_NO_DEPRECATE',
            '_WINSOCK_DEPRECATED_NO_WARNINGS',
            'PX_PHYSX_CORE_EXPORTS',
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
