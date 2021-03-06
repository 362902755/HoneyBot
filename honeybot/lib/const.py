VERSION = '0.7.0'
PT_MAX_BYTES = 5900000 # 5.9 MB (API limit)
CAPTURE_AND_ANALYZE_DESC = 'Capture on an interface for some period of time, and upload capture for analysis.'
TRIGGER_AND_ANALYZE_DESC = 'Listen for unknown connections, and begin capturing when one is made. ' \
                           'Captures are automatically uploaded and analyzed; powered by PacketTotal.com'
UPLOAD_AND_ANALYZE_DESC = 'Upload and analyze .pcap/.pcapng files in bulk; powered by PacketTotal.com.'