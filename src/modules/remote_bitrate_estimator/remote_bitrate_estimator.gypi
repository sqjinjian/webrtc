# Copyright (c) 2011 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'targets': [
    {
      'target_name': 'remote_bitrate_estimator',
      'type': '<(library)',
      'dependencies': [
        # system_wrappers
        '<(webrtc_root)/system_wrappers/source/system_wrappers.gyp:system_wrappers',
      ],
      'include_dirs': [
        'include',
        '../rtp_rtcp/interface',
        '../interface',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'include',
        ],
      },
      'sources': [
        # interface
        'include/bwe_defines.h',
        'include/remote_bitrate_estimator.h',

        # source
        'bitrate_estimator.cc',
        'bitrate_estimator.h',
        'overuse_detector.cc',
        'overuse_detector.h',
        'remote_bitrate_estimator.cc',
        'remote_rate_control.cc',
        'remote_rate_control.h',
      ], # source
    },
  ], # targets
  'conditions': [
    ['include_tests==1', {
      'targets': [
        {
          'target_name': 'remote_bitrate_estimator_unittests',
          'type': 'executable',
          'dependencies': [
            'remote_bitrate_estimator',
            '<(webrtc_root)/../testing/gmock.gyp:gmock',
            '<(webrtc_root)/../testing/gtest.gyp:gtest',
            '<(webrtc_root)/../test/test.gyp:test_support_main',
          ],
          'sources': [
            'include/mock/mock_remote_bitrate_estimator.h',
            'bitrate_estimator_unittest.cc',
            'remote_bitrate_estimator_unittest.cc',
          ],
        },
      ], # targets
    }], # build_with_chromium
  ], # conditions
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
