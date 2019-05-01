#
# PySNMP MIB module CISCO-PROXY-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PROXY-CONTROL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:10:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
cCallHistoryIndex, = mibBuilder.importSymbols("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
CvcGUid, = mibBuilder.importSymbols("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "CvcGUid")
callActiveIndex, AbsoluteCounter32, callActiveSetupTime = mibBuilder.importSymbols("DIAL-CONTROL-MIB", "callActiveIndex", "AbsoluteCounter32", "callActiveSetupTime")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, NotificationType, Bits, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, IpAddress, iso, TimeTicks, Counter32, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Bits", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "IpAddress", "iso", "TimeTicks", "Counter32", "Gauge32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoProxyControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 57))
ciscoProxyControlMIB.setRevisions(('2009-02-11 00:00', '2006-03-12 00:00', '2005-03-06 00:00', '2000-02-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoProxyControlMIB.setRevisionsDescriptions(('[1] Added acronyms for iSAC codecs [2] Added iSAC enum to CProxyAudioCodec textual convention. [3] Added REFERENCE clause to CProxyAudioCodec textual convention for iSAC codec.', '[1] Added acronyms for GSM AMR-NB and iLBC codecs [2] Added iLBC enum to CProxyAudioCodec textual convention. [3] Added REFERENCE clause to CProxyAudioCodec textual convention for GSM AMR-NB and iLBC codecs.', 'Added gsmAmrNb enum to CProxyAudioCodec textual convention.', 'First release of this MIB.',))
if mibBuilder.loadTexts: ciscoProxyControlMIB.setLastUpdated('200902110000Z')
if mibBuilder.loadTexts: ciscoProxyControlMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoProxyControlMIB.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoProxyControlMIB.setDescription('This MIB module enhances the IETF Dial Control MIB (RFC2128) by providing Proxy management information. *** ABBREVIATIONS, ACRONYMS AND SYMBOLS *** GSM - Global System for Mobile Communication AMR-NB - Adaptive Multi Rate - Narrow Band iLBC - internet Low Bitrate Codec iSAC - internet Speech Audio Codec')
ciscoProxyControlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 57, 1))
cProxyCallActive = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1))
cProxyCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2))
class CProxyEndptType(TextualConvention, Integer32):
    description = 'A tag to identify the type of end point that the Proxy is connected to.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("other", 0), ("proxy", 1), ("gateway", 2))

class CProxyAudioCodec(TextualConvention, Integer32):
    reference = '[1] RFC 3267: For introduction about GSM AMR-NB codec, section 3.1 [2] RFC 3952: For introduction about iLBC codec, section 2 [3] iSAC Codec Description Document from GIPS'
    description = 'A tag to identify the type of encoding used to compress the voice data of the call. iLBC - iILBC 13330 or 15200 bps iSAC - iSAC 10 to 32 kbps'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("other", 0), ("nonStandard", 1), ("g711Alawr64k", 2), ("g711Alawr56k", 3), ("g711Ulawr64k", 4), ("g711Ulawr56k", 5), ("g722r64k", 6), ("g722r56k", 7), ("g722r48k", 8), ("g7231", 9), ("g728", 10), ("g729", 11), ("g729AnnexA", 12), ("is11172", 13), ("is13818", 14), ("g729AnnexB", 15), ("g729AnnexAB", 16), ("g729AnnexC", 17), ("gsmFullRate", 18), ("gsmHalfRate", 19), ("gsmEnhancedFullRate", 20), ("gsmAmrNb", 21), ("iLBC", 22), ("iSAC", 23))

class CProxyVideoCodec(TextualConvention, Integer32):
    description = 'A tag to identify the type of encoding used to compress the video data of the call.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 0), ("nonStandard", 1), ("h261", 2), ("h262", 3), ("h263", 4), ("is11172", 5))

cProxyCallActiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1), )
if mibBuilder.loadTexts: cProxyCallActiveTable.setReference('IETF Dial Control MIB (RFC2128)')
if mibBuilder.loadTexts: cProxyCallActiveTable.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveTable.setDescription('This table is the Proxy extension to the call Active table of IETF Dial Control MIB. It contains Proxy call leg information about specific proxied calls.')
cProxyCallActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1), ).setIndexNames((0, "DIAL-CONTROL-MIB", "callActiveSetupTime"), (0, "DIAL-CONTROL-MIB", "callActiveIndex"))
if mibBuilder.loadTexts: cProxyCallActiveEntry.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveEntry.setDescription('The information regarding a single proxied call leg. An entry of this table is created when its associated call Active entry in the IETF Dial Control MIB is created and the call Active entry contains information for the call establishment to the peer on the data network. This entry is deleted when its associated Call Active entry in the IETF Dial Control MIB is deleted.')
cProxyCallActiveConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveConnectionId.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveConnectionId.setDescription('The global call identifier for the Proxy call.')
cProxyCallActiveRemoteIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveRemoteIPAddress.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveRemoteIPAddress.setDescription('Remote system IP address for the call.')
cProxyCallActiveAudioUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveAudioUDPPort.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveAudioUDPPort.setDescription('Remote system UDP listener port to which to transmit voice packets for the call. A value of zero indicates that no port was used.')
cProxyCallActiveVideoUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveVideoUDPPort.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveVideoUDPPort.setDescription('Remote system UDP listener port to which to transmit video packets for the call. A value of zero indicates that no port was used.')
cProxyCallActiveT120TCPPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveT120TCPPort1.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveT120TCPPort1.setDescription('First remote system UDP listener port to which to transmit T120 packets for the call. A value of zero indicates that no port was used.')
cProxyCallActiveT120TCPPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveT120TCPPort2.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveT120TCPPort2.setDescription('Second remote system UDP listener port to which to transmit T120 packets for the call. A value of zero indicates that no port was used.')
cProxyCallActiveT120TCPPort3 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveT120TCPPort3.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveT120TCPPort3.setDescription('Third remote system UDP listener port to which to transmit T120 packets for the call. A value of zero indicates that no port was used.')
cProxyCallActiveT120TCPPort4 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveT120TCPPort4.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveT120TCPPort4.setDescription('Fourth remote system UDP listener port to which to transmit T120 packets for the call. A value of zero indicates that no port was used.')
cProxyCallActiveEndpointType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 9), CProxyEndptType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveEndpointType.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveEndpointType.setDescription('The type of end point this proxy call leg is connected to.')
cProxyCallActiveEndpointVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveEndpointVendor.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveEndpointVendor.setDescription('The H225 Manufacturers code for this endpoint. Zero indicates unknown vendor.')
cProxyCallActiveRequestBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000000))).setUnits('kilobits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveRequestBandwidth.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveRequestBandwidth.setDescription('The requested bandwidth for this proxied call leg.')
cProxyCallActiveActualBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000000))).setUnits('kilobits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveActualBandwidth.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveActualBandwidth.setDescription('The actual bandwidth used by the proxied call.')
cProxyCallActiveAudioCoderRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 13), CProxyAudioCodec()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveAudioCoderRate.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveAudioCoderRate.setDescription('The negotiated coder rate. It specifies the transmit rate of audio compression to its associated call leg for the call.')
cProxyCallActiveVideoCoderRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 14), CProxyVideoCodec()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveVideoCoderRate.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveVideoCoderRate.setDescription('The negotiated coder rate. It specifies the transmit rate of video compression to its associated call leg for the call.')
cProxyCallActiveRxAudioPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 15), AbsoluteCounter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveRxAudioPackets.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveRxAudioPackets.setDescription('The number of audio packets received from the remote end for this call.')
cProxyCallActiveRxAudioBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 16), AbsoluteCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveRxAudioBytes.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveRxAudioBytes.setDescription('The number of audio bytes received from the remote end for this call.')
cProxyCallActiveTxAudioPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 17), AbsoluteCounter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveTxAudioPackets.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveTxAudioPackets.setDescription('The number of audio packets transmitted to the remote end for this call.')
cProxyCallActiveTxAudioBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 18), AbsoluteCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveTxAudioBytes.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveTxAudioBytes.setDescription('The number of audio bytes transmitted to the remote end for this call.')
cProxyCallActiveRxVideoPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 19), AbsoluteCounter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveRxVideoPackets.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveRxVideoPackets.setDescription('The number of video packets received from the remote end for this call.')
cProxyCallActiveRxVideoBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 20), AbsoluteCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveRxVideoBytes.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveRxVideoBytes.setDescription('The number of video bytes received from the remote end for this call.')
cProxyCallActiveTxVideoPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 21), AbsoluteCounter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveTxVideoPackets.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveTxVideoPackets.setDescription('The number of video packets transmitted to the remote end for this call.')
cProxyCallActiveTxVideoBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 22), AbsoluteCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveTxVideoBytes.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveTxVideoBytes.setDescription('The number of video bytes transmitted to the remote end for this call.')
cProxyCallActiveRxT120Packets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 23), AbsoluteCounter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveRxT120Packets.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveRxT120Packets.setDescription('The number of T120 data packets received from the remote end for this call.')
cProxyCallActiveRxT120Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 24), AbsoluteCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveRxT120Bytes.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveRxT120Bytes.setDescription('The number of T120 data bytes received from the remote end of this call.')
cProxyCallActiveTxT120Packets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 25), AbsoluteCounter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveTxT120Packets.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveTxT120Packets.setDescription('The number of T120 data packets transmitted to the remote end for this call.')
cProxyCallActiveTxT120Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 26), AbsoluteCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallActiveTxT120Bytes.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveTxT120Bytes.setDescription('The number of T120 data bytes transmitted to the remote end of this call.')
cProxyCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1), )
if mibBuilder.loadTexts: cProxyCallHistoryTable.setReference('IETF Dial Control MIB (RFC2128)')
if mibBuilder.loadTexts: cProxyCallHistoryTable.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryTable.setDescription('This table is the Proxy extension to the History call table of IETF Dial Control MIB. It contains PROXY call leg information about proxied call.')
cProxyCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cProxyCallHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryEntry.setDescription('The information regarding a single proxied call leg. An entry of this table is created when its associated call History entry in the IETF Dial Control MIB is created. The call History entry contains information for the call establishment to the peer on the data network backbone via a voice over PROXY peer. The entry is deleted when its associated call History entry in the IETF Dial Control MIB is deleted.')
cProxyCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryConnectionId.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryConnectionId.setDescription('The global call identifier for the Proxy call.')
cProxyCallHistoryRemoteIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryRemoteIPAddress.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryRemoteIPAddress.setDescription('Remote system IP address for the call.')
cProxyCallHistoryAudioUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryAudioUDPPort.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryAudioUDPPort.setDescription('Remote system UDP listener port to which to transmit voice packets for the call. A value of zero indicates that no port was used.')
cProxyCallHistoryVideoUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryVideoUDPPort.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryVideoUDPPort.setDescription('Remote system UDP listener port to which to transmit video packets for the call. A value of zero indicates that no port was used.')
cProxyCallHistoryT120TCPPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryT120TCPPort1.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryT120TCPPort1.setDescription('First remote system UDP listener port to which to transmit T120 packets for the call. A value of zero indicates that no port was used.')
cProxyCallHistoryT120TCPPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryT120TCPPort2.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryT120TCPPort2.setDescription('Second remote system UDP listener port to which to transmit T120 packets for the call. A value of zero indicates that no port was used.')
cProxyCallHistoryT120TCPPort3 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryT120TCPPort3.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryT120TCPPort3.setDescription('Third remote system UDP listener port to which to transmit T120 packets for the call. A value of zero indicates that no port was used.')
cProxyCallHistoryT120TCPPort4 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryT120TCPPort4.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryT120TCPPort4.setDescription('Fourth remote system UDP listener port to which to transmit T120 packets for the call. A value of zero indicates that no port was used.')
cProxyCallHistoryEndpointType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 9), CProxyEndptType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryEndpointType.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryEndpointType.setDescription('The type of end point this proxy call leg is connected to.')
cProxyCallHistoryEndpointVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryEndpointVendor.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryEndpointVendor.setDescription('The H225 Manufacturers code for this endpoint. Zero indicates unknown vendor.')
cProxyCallHistoryRequestBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000000))).setUnits('kilobits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryRequestBandwidth.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryRequestBandwidth.setDescription('The requested bandwidth for this proxied call leg.')
cProxyCallHistoryActualBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000000))).setUnits('kilobits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryActualBandwidth.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryActualBandwidth.setDescription('The actual bandwidth used by the proxied call.')
cProxyCallHistoryAudioCoderRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 13), CProxyAudioCodec()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryAudioCoderRate.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryAudioCoderRate.setDescription('The negotiated coder rate. It specifies the transmit rate of audio compression to its associated call leg for the call.')
cProxyCallHistoryVideoCoderRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 14), CProxyVideoCodec()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryVideoCoderRate.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryVideoCoderRate.setDescription('The negotiated coder rate. It specifies the transmit rate of video compression to its associated call leg for the call.')
cProxyCallHistoryRxAudioPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 15), AbsoluteCounter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryRxAudioPackets.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryRxAudioPackets.setDescription('The number of audio packets received from the remote end for this call.')
cProxyCallHistoryRxAudioBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 16), AbsoluteCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryRxAudioBytes.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryRxAudioBytes.setDescription('The number of audio bytes received from the remote end for this call.')
cProxyCallHistoryTxAudioPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 17), AbsoluteCounter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryTxAudioPackets.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryTxAudioPackets.setDescription('The number of audio packets transmitted to the remote end for this call.')
cProxyCallHistoryTxAudioBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 18), AbsoluteCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryTxAudioBytes.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryTxAudioBytes.setDescription('The number of audio bytes transmitted to the remote end for this call.')
cProxyCallHistoryRxVideoPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 19), AbsoluteCounter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryRxVideoPackets.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryRxVideoPackets.setDescription('The number of video packets received from the remote end for this call.')
cProxyCallHistoryRxVideoBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 20), AbsoluteCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryRxVideoBytes.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryRxVideoBytes.setDescription('The number of video bytes received from the remote end for this call.')
cProxyCallHistoryTxVideoPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 21), AbsoluteCounter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryTxVideoPackets.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryTxVideoPackets.setDescription('The number of video packets transmitted to the remote end for this call.')
cProxyCallHistoryTxVideoBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 22), AbsoluteCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryTxVideoBytes.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryTxVideoBytes.setDescription('The number of video bytes transmitted to the remote end for this call.')
cProxyCallHistoryRxT120Packets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 23), AbsoluteCounter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryRxT120Packets.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryRxT120Packets.setDescription('The number of T120 data packets received from the remote end for this call.')
cProxyCallHistoryRxT120Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 24), AbsoluteCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryRxT120Bytes.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryRxT120Bytes.setDescription('The number of T120 data bytes received from the remote end for this call.')
cProxyCallHistoryTxT120Packets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 25), AbsoluteCounter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryTxT120Packets.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryTxT120Packets.setDescription('The number of T120 data packets transmitted to the remote end for this call.')
cProxyCallHistoryTxT120Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 26), AbsoluteCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cProxyCallHistoryTxT120Bytes.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryTxT120Bytes.setDescription('The number of T120 data bytes transmitted to the remote end for this call.')
ciscoProxyControlMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 57, 2))
ciscoProxyControlMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 57, 2, 0))
ciscoProxyControlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 57, 3))
ciscoProxyControlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 57, 3, 1))
ciscoProxyControlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 57, 3, 2))
ciscoProxyControlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 57, 3, 1, 1)).setObjects(("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveGroup"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProxyControlMIBCompliance = ciscoProxyControlMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoProxyControlMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO PROXY CONTROL MIB')
cProxyCallActiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 57, 3, 2, 1)).setObjects(("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveConnectionId"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRemoteIPAddress"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveAudioUDPPort"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveVideoUDPPort"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveT120TCPPort1"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveT120TCPPort2"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveT120TCPPort3"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveT120TCPPort4"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveEndpointType"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveEndpointVendor"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRequestBandwidth"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveActualBandwidth"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveAudioCoderRate"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveVideoCoderRate"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRxAudioPackets"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRxAudioBytes"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveTxAudioPackets"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveTxAudioBytes"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRxVideoPackets"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRxVideoBytes"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveTxVideoPackets"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveTxVideoBytes"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRxT120Packets"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRxT120Bytes"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveTxT120Packets"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveTxT120Bytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cProxyCallActiveGroup = cProxyCallActiveGroup.setStatus('current')
if mibBuilder.loadTexts: cProxyCallActiveGroup.setDescription('A collection of objects providing the PROXY Call Active entry capability.')
cProxyCallHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 57, 3, 2, 2)).setObjects(("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryConnectionId"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRemoteIPAddress"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryAudioUDPPort"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryVideoUDPPort"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryT120TCPPort1"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryT120TCPPort2"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryT120TCPPort3"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryT120TCPPort4"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryEndpointType"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryEndpointVendor"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRequestBandwidth"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryActualBandwidth"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryAudioCoderRate"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryVideoCoderRate"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRxAudioPackets"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRxAudioBytes"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryTxAudioPackets"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryTxAudioBytes"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRxVideoPackets"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRxVideoBytes"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryTxVideoPackets"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryTxVideoBytes"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRxT120Packets"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRxT120Bytes"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryTxT120Packets"), ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryTxT120Bytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cProxyCallHistoryGroup = cProxyCallHistoryGroup.setStatus('current')
if mibBuilder.loadTexts: cProxyCallHistoryGroup.setDescription('A collection of objects providing the PROXY Call Active entry capability.')
mibBuilder.exportSymbols("CISCO-PROXY-CONTROL-MIB", cProxyCallActiveGroup=cProxyCallActiveGroup, cProxyCallActiveRxAudioPackets=cProxyCallActiveRxAudioPackets, cProxyCallActiveEndpointVendor=cProxyCallActiveEndpointVendor, cProxyCallHistoryConnectionId=cProxyCallHistoryConnectionId, cProxyCallHistoryVideoCoderRate=cProxyCallHistoryVideoCoderRate, cProxyCallHistory=cProxyCallHistory, cProxyCallHistoryRxVideoBytes=cProxyCallHistoryRxVideoBytes, cProxyCallActiveVideoCoderRate=cProxyCallActiveVideoCoderRate, cProxyCallActiveRequestBandwidth=cProxyCallActiveRequestBandwidth, CProxyVideoCodec=CProxyVideoCodec, cProxyCallActiveAudioCoderRate=cProxyCallActiveAudioCoderRate, cProxyCallHistoryTxT120Packets=cProxyCallHistoryTxT120Packets, cProxyCallHistoryEndpointType=cProxyCallHistoryEndpointType, cProxyCallHistoryEntry=cProxyCallHistoryEntry, cProxyCallActiveEndpointType=cProxyCallActiveEndpointType, ciscoProxyControlMIBCompliance=ciscoProxyControlMIBCompliance, cProxyCallActiveRxAudioBytes=cProxyCallActiveRxAudioBytes, ciscoProxyControlMIB=ciscoProxyControlMIB, cProxyCallActiveT120TCPPort1=cProxyCallActiveT120TCPPort1, cProxyCallActiveT120TCPPort4=cProxyCallActiveT120TCPPort4, cProxyCallActiveTxAudioBytes=cProxyCallActiveTxAudioBytes, PYSNMP_MODULE_ID=ciscoProxyControlMIB, cProxyCallHistoryT120TCPPort2=cProxyCallHistoryT120TCPPort2, cProxyCallActiveRxVideoBytes=cProxyCallActiveRxVideoBytes, cProxyCallHistoryVideoUDPPort=cProxyCallHistoryVideoUDPPort, cProxyCallHistoryT120TCPPort4=cProxyCallHistoryT120TCPPort4, cProxyCallHistoryTxAudioPackets=cProxyCallHistoryTxAudioPackets, cProxyCallHistoryRxT120Bytes=cProxyCallHistoryRxT120Bytes, cProxyCallActiveTxVideoBytes=cProxyCallActiveTxVideoBytes, cProxyCallActiveTxT120Bytes=cProxyCallActiveTxT120Bytes, cProxyCallHistoryT120TCPPort3=cProxyCallHistoryT120TCPPort3, cProxyCallActiveRxT120Bytes=cProxyCallActiveRxT120Bytes, cProxyCallHistoryRxAudioPackets=cProxyCallHistoryRxAudioPackets, ciscoProxyControlMIBObjects=ciscoProxyControlMIBObjects, cProxyCallActiveTable=cProxyCallActiveTable, cProxyCallActiveTxAudioPackets=cProxyCallActiveTxAudioPackets, cProxyCallHistoryRxVideoPackets=cProxyCallHistoryRxVideoPackets, ciscoProxyControlMIBNotifications=ciscoProxyControlMIBNotifications, ciscoProxyControlMIBCompliances=ciscoProxyControlMIBCompliances, cProxyCallActiveConnectionId=cProxyCallActiveConnectionId, cProxyCallHistoryActualBandwidth=cProxyCallHistoryActualBandwidth, cProxyCallHistoryTxAudioBytes=cProxyCallHistoryTxAudioBytes, ciscoProxyControlMIBGroups=ciscoProxyControlMIBGroups, cProxyCallActiveT120TCPPort2=cProxyCallActiveT120TCPPort2, cProxyCallHistoryRxAudioBytes=cProxyCallHistoryRxAudioBytes, cProxyCallActiveVideoUDPPort=cProxyCallActiveVideoUDPPort, cProxyCallHistoryTable=cProxyCallHistoryTable, cProxyCallActiveTxT120Packets=cProxyCallActiveTxT120Packets, cProxyCallActive=cProxyCallActive, cProxyCallHistoryEndpointVendor=cProxyCallHistoryEndpointVendor, cProxyCallHistoryT120TCPPort1=cProxyCallHistoryT120TCPPort1, cProxyCallHistoryTxVideoPackets=cProxyCallHistoryTxVideoPackets, ciscoProxyControlMIBConformance=ciscoProxyControlMIBConformance, cProxyCallHistoryGroup=cProxyCallHistoryGroup, cProxyCallActiveRemoteIPAddress=cProxyCallActiveRemoteIPAddress, cProxyCallHistoryAudioUDPPort=cProxyCallHistoryAudioUDPPort, cProxyCallHistoryRxT120Packets=cProxyCallHistoryRxT120Packets, cProxyCallActiveAudioUDPPort=cProxyCallActiveAudioUDPPort, cProxyCallActiveEntry=cProxyCallActiveEntry, cProxyCallActiveTxVideoPackets=cProxyCallActiveTxVideoPackets, cProxyCallHistoryRemoteIPAddress=cProxyCallHistoryRemoteIPAddress, cProxyCallActiveRxT120Packets=cProxyCallActiveRxT120Packets, cProxyCallActiveT120TCPPort3=cProxyCallActiveT120TCPPort3, cProxyCallActiveRxVideoPackets=cProxyCallActiveRxVideoPackets, cProxyCallActiveActualBandwidth=cProxyCallActiveActualBandwidth, cProxyCallHistoryRequestBandwidth=cProxyCallHistoryRequestBandwidth, cProxyCallHistoryTxT120Bytes=cProxyCallHistoryTxT120Bytes, ciscoProxyControlMIBNotificationPrefix=ciscoProxyControlMIBNotificationPrefix, CProxyAudioCodec=CProxyAudioCodec, cProxyCallHistoryTxVideoBytes=cProxyCallHistoryTxVideoBytes, cProxyCallHistoryAudioCoderRate=cProxyCallHistoryAudioCoderRate, CProxyEndptType=CProxyEndptType)
