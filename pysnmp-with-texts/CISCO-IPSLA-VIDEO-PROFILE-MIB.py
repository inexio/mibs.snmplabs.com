#
# PySNMP MIB module CISCO-IPSLA-VIDEO-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSLA-VIDEO-PROFILE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:02:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CvcVideoProfile, = mibBuilder.importSymbols("CISCO-VIDEO-SESSION-MIB", "CvcVideoProfile")
CvcVideoResolution, = mibBuilder.importSymbols("CISCO-VIDEO-TC", "CvcVideoResolution")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, Unsigned32, Bits, MibIdentifier, Counter32, IpAddress, NotificationType, Integer32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Bits", "MibIdentifier", "Counter32", "IpAddress", "NotificationType", "Integer32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "ObjectIdentity")
TextualConvention, StorageType, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "RowStatus", "DisplayString")
ciscoIpslaVideoProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 766))
ciscoIpslaVideoProfileMIB.setRevisions(('2011-01-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpslaVideoProfileMIB.setRevisionsDescriptions(('initial version of the MIB',))
if mibBuilder.loadTexts: ciscoIpslaVideoProfileMIB.setLastUpdated('201101240000Z')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileMIB.setDescription("IP SLA is a capability which utilizes active monitoring for network performance. It can be used for network troubleshooting, network assessment and health monitoring. This MIB defines the following table as the collection of IP SLA video traffic profiles that are used when generating synthetic video traffic by configured IP SLA video operations. cipslaVideoProfileTable To run an IP SLA Video Operation, the MIB user should do the following configurations: 1. Create a new or reuse the existing rttMonEchoAdminEntry with valid rttMonEchoAdminProtocol, rttMonEchoAdminTargetAddress, rttMonEchoAdminTargetPort, rttMonEchoAdminSourceAddress, rttMonEchoAdminSourcePort, rttMonEchoAdminVideoTrafficProfile, rttMonEchoAdminDscp, rttMonEchoAdminReserveDsp, rttMonEchoAdminInputInterface, and other applicable objects (if any) in rttMonEchoAdminTable of CISCO-RTTMON-MIB. 2. Schedule the operation to run immediately or at some scheduled time(s) with optional recurrence(s) if desirable, by configuring with rttMonCtrlAdminTable of CISCO-RTTMON-MIB. 3. Each occurrance of the scheduled operation generates a report for the IP SLA VO statistics which are populated and available in cipslaLatestVideoStatsTable and cipslaVideoAggStatsTable of CISCO-IPSLA-VIDEO-MIB. Glossary: IP SLA - Cisco IOS IP Service Level Agreements IP SLA operation - Refers to the 'video' operation supported by IP SLA. RTT - Round Trip Time")
ciscoIpslaVideoProfileMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 766, 0))
ciscoIpslaVideoProfileMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 766, 1))
ciscoIpslaVideoProfileMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 766, 2))
ciscoIpslaVideoProfileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 766, 2, 1))
cipslaVideoProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1))
cipslaVideoProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1), )
if mibBuilder.loadTexts: cipslaVideoProfileTable.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileTable.setDescription('This table lists the definitions of IP SLA video profiles that contain descriptive parameters for synthetic video traffic patterns which can be used when generating synthetic video packets by IP SLA Video Operation.')
cipslaVideoProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileID"))
if mibBuilder.loadTexts: cipslaVideoProfileEntry.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileEntry.setDescription('A conceptual row in the cipslaVideoProfileTable')
cipslaVideoProfileID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cipslaVideoProfileID.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileID.setDescription('An arbitrary index that uniquely identifies a video profile')
cipslaVideoProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileRowStatus.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileRowStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table.')
cipslaVideoProfileStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 3), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileStorageType.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileStorageType.setDescription('This object specifies the storage type for this conceptual row. The following columnar objects are allowed to be writable when the storageType of this conceptual row is permanent(4): cipslaVideoProfileDescription cipslaVideoProfileEndpointType cipslaVideoProfileCodec cipslaVideoProfileVideoContents cipslaVideoProfileFrameRate cipslaVideoProfileResolution cipslaVideoProfileAvgBitrate cipslaVideoProfileMaxBitrate cipslaVideoProfileMinBitrate cipslaVideoProfileBitrateWindowSize cipslaVideoProfileIframeMaxSize cipslaVideoProfileIframeRefreshInterval cipslaVideoProfileRtpAvgSize cipslaVideoProfileRtpJitterPattern')
cipslaVideoProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileName.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileName.setDescription('This object specifies the name of an IP SLA video profile.')
cipslaVideoProfileDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileDescription.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileDescription.setDescription('This object specifies the detailed description string of this video profile.')
cipslaVideoProfileEndpointType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 21, 22, 31, 9999))).clone(namedValues=NamedValues(("custom", 1), ("cts1k", 21), ("cts3k", 22), ("cp99xx", 31), ("unknown", 9999)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileEndpointType.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileEndpointType.setDescription("This object specifies the sender endpoint type which determines the traffic pattern according to the encoder's characteristics while generating and sending video packets. custom - Allows flexibile endpoint behavior cts1k - Cisco Telepresence System CTS-1000 cts3k - Cisco Telepresence System CTS-3000 cp99xx - Cisco CP-9900 series video IP phones unknown - unknown endpoint type")
cipslaVideoProfileCodec = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 7), CvcVideoProfile().clone('h264ProfileBaseline')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileCodec.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileCodec.setDescription('This object specifies the video codec and codec profile for how the video contents are encoded in byte streams.')
cipslaVideoProfileVideoContents = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 255))).clone(namedValues=NamedValues(("conferenceRoom", 1), ("singlePerson", 2), ("presentation", 3), ("sports", 4), ("streetView", 5), ("other", 255))).clone('singlePerson')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileVideoContents.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileVideoContents.setDescription('This object specifies the video contents that determine the amount of information to be encoded by the video sender and thus have effects on the peak rate and frame size in the video traffic generation. This gives a high level description of the traffic patterns, and can be overwritten by the detailed parameters such as cipslaVideoProfileIframeRefreshInterval. The supported video contents are as follows. conferenceRoom - conference room scene singlePerson - single person in video conferencing presentation - presentation video sports - sports activities video streetView - video scene from street views other - other scenes')
cipslaVideoProfileFrameRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 120000))).setUnits('fpks').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileFrameRate.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileFrameRate.setDescription("This object specifies the video frame rates in the generated video traffic, in unit of 'frames per 1K seconds' or fpks. For example, 30000 means 30 frames per second (fps), and 7500 means 7.5 fps. The maximum frame rate is 120 fps or 120000 fpks.")
cipslaVideoProfileResolution = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 10), CvcVideoResolution()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileResolution.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileResolution.setDescription('This object specifies the video frame resolution of the generated video traffic.')
cipslaVideoProfileAvgBitrate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 24000))).setUnits('kbps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileAvgBitrate.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileAvgBitrate.setDescription("This object specifies the average bit rate of a video traffic pattern in kilo-bits per second. It is used by the sender's encoder to upper-limit the generated video packets.")
cipslaVideoProfileMaxBitrate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 240000))).setUnits('kbps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileMaxBitrate.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileMaxBitrate.setDescription("This object specifies the maximum bit rate or peak rate of the video traffic that can be generated by the sender's encoder, in kilo-bits per second. This value is valid only in the range from the average bit rate to 10 times the average bit rate, where the average bit rate is specified in cipslaVideoProfileAvgBitrate object.")
cipslaVideoProfileMinBitrate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 24000))).setUnits('kbps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileMinBitrate.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileMinBitrate.setDescription('This object specifies the minimum bit rate in kilo-bits per second, at which the video traffic can be generated even when the video contents are still. This value is valid only in the range from 1 to the average bit rate as specified in cipslaVideoProfileAvgBitrate object.')
cipslaVideoProfileBitrateWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000)).clone(500)).setUnits('ms').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileBitrateWindowSize.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileBitrateWindowSize.setDescription('This object specifies the rate control window size which is used by the video encoder to calculate the running average bit rate. The smaller the value of this bit rate window size, less bursty of the traffic; this bitrate control window size is specified in milliseconds. Value 0 indicates no bitrate window control.')
cipslaVideoProfileIframeMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(50)).setUnits('kB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileIframeMaxSize.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileIframeMaxSize.setDescription('This object specifies the maximum size of an I-frame that the video encoder can generate, in kilo-bytes.')
cipslaVideoProfileIframeRefreshInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setUnits('ms').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileIframeRefreshInterval.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileIframeRefreshInterval.setDescription('This object specifies the refresh-rate of video intra-frames, in seconds. Value 0 indicates that only the first frame is an intra-frame, i.e no refresh.')
cipslaVideoProfileRtpAvgSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(500, 1600)).clone(1000)).setUnits('byte').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileRtpAvgSize.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileRtpAvgSize.setDescription('This object specifies the average RTP packet size in generated video traffic, in bytes.')
cipslaVideoProfileRtpJitterPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 766, 1, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 99))).clone(namedValues=NamedValues(("bursty", 1), ("shaped", 2), ("other", 99))).clone('bursty')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaVideoProfileRtpJitterPattern.setStatus('current')
if mibBuilder.loadTexts: cipslaVideoProfileRtpJitterPattern.setDescription('This object specifies the output buffering control mechanism of the video encoder when generating packets. bursty - send packets all out at once, no buffering shaped - send packets evenly in a frame interval, with buffering other - other patterns')
ciscoIpslaVideoProfileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 766, 2, 2))
ciscoIpslaVideoProfileMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 766, 2, 1, 1)).setObjects(("CISCO-IPSLA-VIDEO-PROFILE-MIB", "ciscoIpslaVideoProfileBaseGroup"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "ciscoIpslaVideoProfileIsrg2Pvdm3Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileMIBCompliance = ciscoIpslaVideoProfileMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileMIBCompliance.setDescription('This is the module-compliance for ISR G2 with PVDM3 platforms, containing object groups and notification groups.')
ciscoIpslaVideoProfileBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 766, 2, 2, 1)).setObjects(("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileRowStatus"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileStorageType"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileDescription"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileBaseGroup = ciscoIpslaVideoProfileBaseGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileBaseGroup.setDescription('The is the base group to include those objects for all platforms implementations.')
ciscoIpslaVideoProfileIsrg2Pvdm3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 766, 2, 2, 2)).setObjects(("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileEndpointType"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileCodec"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileVideoContents"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileFrameRate"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileResolution"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileAvgBitrate"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileMaxBitrate"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileMinBitrate"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileBitrateWindowSize"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileIframeMaxSize"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileIframeRefreshInterval"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileRtpAvgSize"), ("CISCO-IPSLA-VIDEO-PROFILE-MIB", "cipslaVideoProfileRtpJitterPattern"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileIsrg2Pvdm3Group = ciscoIpslaVideoProfileIsrg2Pvdm3Group.setStatus('current')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileIsrg2Pvdm3Group.setDescription('This is the object group to include those objects that are only applicable to Cisco ISR G2 platforms with PVDM3.')
mibBuilder.exportSymbols("CISCO-IPSLA-VIDEO-PROFILE-MIB", cipslaVideoProfileAvgBitrate=cipslaVideoProfileAvgBitrate, cipslaVideoProfileFrameRate=cipslaVideoProfileFrameRate, cipslaVideoProfileRtpJitterPattern=cipslaVideoProfileRtpJitterPattern, cipslaVideoProfileStorageType=cipslaVideoProfileStorageType, cipslaVideoProfile=cipslaVideoProfile, cipslaVideoProfileMinBitrate=cipslaVideoProfileMinBitrate, ciscoIpslaVideoProfileMIBCompliances=ciscoIpslaVideoProfileMIBCompliances, cipslaVideoProfileTable=cipslaVideoProfileTable, cipslaVideoProfileEntry=cipslaVideoProfileEntry, ciscoIpslaVideoProfileMIBNotifs=ciscoIpslaVideoProfileMIBNotifs, cipslaVideoProfileMaxBitrate=cipslaVideoProfileMaxBitrate, cipslaVideoProfileEndpointType=cipslaVideoProfileEndpointType, cipslaVideoProfileIframeRefreshInterval=cipslaVideoProfileIframeRefreshInterval, ciscoIpslaVideoProfileMIBConform=ciscoIpslaVideoProfileMIBConform, cipslaVideoProfileName=cipslaVideoProfileName, cipslaVideoProfileCodec=cipslaVideoProfileCodec, cipslaVideoProfileDescription=cipslaVideoProfileDescription, cipslaVideoProfileIframeMaxSize=cipslaVideoProfileIframeMaxSize, ciscoIpslaVideoProfileBaseGroup=ciscoIpslaVideoProfileBaseGroup, cipslaVideoProfileID=cipslaVideoProfileID, ciscoIpslaVideoProfileMIBObjects=ciscoIpslaVideoProfileMIBObjects, ciscoIpslaVideoProfileMIBCompliance=ciscoIpslaVideoProfileMIBCompliance, PYSNMP_MODULE_ID=ciscoIpslaVideoProfileMIB, ciscoIpslaVideoProfileMIBGroups=ciscoIpslaVideoProfileMIBGroups, cipslaVideoProfileVideoContents=cipslaVideoProfileVideoContents, cipslaVideoProfileBitrateWindowSize=cipslaVideoProfileBitrateWindowSize, cipslaVideoProfileRtpAvgSize=cipslaVideoProfileRtpAvgSize, ciscoIpslaVideoProfileMIB=ciscoIpslaVideoProfileMIB, cipslaVideoProfileResolution=cipslaVideoProfileResolution, ciscoIpslaVideoProfileIsrg2Pvdm3Group=ciscoIpslaVideoProfileIsrg2Pvdm3Group, cipslaVideoProfileRowStatus=cipslaVideoProfileRowStatus)
