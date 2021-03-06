#
# PySNMP MIB module A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:07:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cVoice, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cVoice")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
AbsoluteCounter32, = mibBuilder.importSymbols("DIAL-CONTROL-MIB", "AbsoluteCounter32")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, NotificationType, Counter32, TimeTicks, Counter64, MibIdentifier, ObjectIdentity, ModuleIdentity, iso, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "NotificationType", "Counter32", "TimeTicks", "Counter64", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
h3cVoiceEntityControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14))
h3cVoiceEntityControl.setRevisions(('2009-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cVoiceEntityControl.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: h3cVoiceEntityControl.setLastUpdated('200904160000Z')
if mibBuilder.loadTexts: h3cVoiceEntityControl.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cVoiceEntityControl.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: h3cVoiceEntityControl.setDescription('This MIB file is to provide the definition of voice dial control configuration.')
class H3cCodecType(TextualConvention, Integer32):
    description = 'Type of Codec.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("g711a", 1), ("g711u", 2), ("g723r53", 3), ("g723r63", 4), ("g729r8", 5), ("g729a", 6), ("g726r16", 7), ("g726r24", 8), ("g726r32", 9), ("g726r40", 10), ("unknown", 11), ("g729br8", 12))

class H3cOutBandMode(TextualConvention, Integer32):
    description = 'Type of OutBandMode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("voice", 1), ("h245AlphaNumeric", 2), ("h225", 3), ("sip", 4), ("nte", 5), ("vofr", 6))

class H3cFaxProtocolType(TextualConvention, Integer32):
    description = 'Type of FaxProtocol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("t38", 1), ("standardt38", 2), ("pcmG711alaw", 3), ("pcmG711ulaw", 4))

class H3cFaxBaudrateType(TextualConvention, Integer32):
    description = 'Type of FaxBaudrate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("disable", 1), ("voice", 2), ("b2400", 3), ("b4800", 4), ("b9600", 5), ("b14400", 6))

class H3cFaxTrainMode(TextualConvention, Integer32):
    description = 'Type of FaxTrainMode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("local", 1), ("ppp", 2))

class H3cRegisterdStatus(TextualConvention, Integer32):
    description = 'Type of Registerd Status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("offline", 2), ("online", 3), ("login", 4), ("logout", 5))

h3cVoEntityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1))
h3cVoEntityCreateTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 1), )
if mibBuilder.loadTexts: h3cVoEntityCreateTable.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCreateTable.setDescription('The table contains the voice entity information that is used to create an ifIndexed row.')
h3cVoEntityCreateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB", "h3cVoEntityIndex"))
if mibBuilder.loadTexts: h3cVoEntityCreateEntry.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCreateEntry.setDescription('The entry of h3cVoEntityCreateTable.')
h3cVoEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoEntityIndex.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityIndex.setDescription('An arbitrary index that uniquely identifies a voice entity.')
h3cVoEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pots", 1), ("voip", 2), ("vofr", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoEntityType.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityType.setDescription('Specify the type of voice related encapsulation.')
h3cVoEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoEntityRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityRowStatus.setDescription(' This object is used to create, delete or modify a row in this table. The h3cVoEntityType object should not be modified once the new row has been created.')
h3cVoEntityCommonConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2), )
if mibBuilder.loadTexts: h3cVoEntityCommonConfigTable.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCommonConfigTable.setDescription('This table contains the general voice entity information.')
h3cVoEntityCommonConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB", "h3cVoEntityCfgIndex"))
if mibBuilder.loadTexts: h3cVoEntityCommonConfigEntry.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCommonConfigEntry.setDescription('The entry of h3cVoEntityCommonConfigTable.')
h3cVoEntityCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoEntityCfgIndex.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgIndex.setDescription('An arbitrary index that uniquely identifies a voice entity.')
h3cVoEntityCfgCodec1st = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 2), H3cCodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgCodec1st.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgCodec1st.setDescription('This object indicates the first desirable CODEC of speech of this dial entity.')
h3cVoEntityCfgCodec2nd = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 3), H3cCodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgCodec2nd.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgCodec2nd.setDescription('This object indicates the second desirable CODEC of speech of this dial entity.')
h3cVoEntityCfgCodec3rd = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 4), H3cCodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgCodec3rd.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgCodec3rd.setDescription('This object indicates the third desirable CODEC of speech of this dial entity.')
h3cVoEntityCfgCodec4th = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 5), H3cCodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgCodec4th.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgCodec4th.setDescription('This object indicates the forth desirable CODEC of speech of this dial entity.')
h3cVoEntityCfgDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgDSCP.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgDSCP.setDescription('This object indicates the DSCP(Different Service Code Point) value of voice packets.')
h3cVoEntityCfgVADEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgVADEnable.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgVADEnable.setDescription('This object indicates whether the VAD(Voice Activity Detection) is enabled.')
h3cVoEntityCfgOutbandMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 8), H3cOutBandMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgOutbandMode.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgOutbandMode.setDescription('This object indicates the DTMF(Dual Tone Multi-Frequency) outband type of this dial entity.')
h3cVoEntityCfgFaxLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, -3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxLevel.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgFaxLevel.setDescription('This object indicates the fax level of this dial entity.')
h3cVoEntityCfgFaxBaudrate = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 10), H3cFaxBaudrateType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxBaudrate.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgFaxBaudrate.setDescription('This object indicates the fax baudrate of this dial entity.')
h3cVoEntityCfgFaxLocalTrainPara = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxLocalTrainPara.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgFaxLocalTrainPara.setDescription('This object indicates the fax local train threshold of this dial entity.')
h3cVoEntityCfgFaxProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 12), H3cFaxProtocolType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxProtocol.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgFaxProtocol.setDescription('This object indicates the fax protocol of this dial entity.')
h3cVoEntityCfgFaxHRPackNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxHRPackNum.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgFaxHRPackNum.setDescription('This object indicates the high speed redundancy packet numbers of t38 and standard-t38.')
h3cVoEntityCfgFaxLRPackNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxLRPackNum.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgFaxLRPackNum.setDescription('This object indicates the low speed redundancy packet numbers of t38 and standard-t38.')
h3cVoEntityCfgFaxSendNSFEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxSendNSFEnable.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgFaxSendNSFEnable.setDescription('This object indicates whether sends NSF(Non-Standard Faculty) to fax of this dial entity.')
h3cVoEntityCfgFaxTrainMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 16), H3cFaxTrainMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxTrainMode.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgFaxTrainMode.setDescription('This object indicates the fax train mode of this dial entity.')
h3cVoEntityCfgFaxEcm = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 17), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgFaxEcm.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgFaxEcm.setDescription('This object indicates whether the ECM(Error Correct Mode) is enabled.')
h3cVoEntityCfgPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgPriority.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgPriority.setDescription('This object indicates the priority of this dial entity.')
h3cVoEntityCfgDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 2, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityCfgDescription.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityCfgDescription.setDescription('This object indicates the textual description of this dial entity.')
h3cVoPOTSEntityConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 3), )
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigTable.setStatus('current')
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigTable.setDescription('This table contains the POTS(Public Switched Telephone Network) entity information.')
h3cVoPOTSEntityConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB", "h3cVoPOTSEntityConfigIndex"))
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigEntry.setStatus('current')
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigEntry.setDescription('The entry of h3cVoPOTSEntityConfigTable.')
h3cVoPOTSEntityConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigIndex.setStatus('current')
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigIndex.setDescription('An arbitrary index that uniquely identifies a voice entity.')
h3cVoPOTSEntityConfigPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigPrefix.setStatus('current')
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigPrefix.setDescription('This object indicates the prefix which is added to the called number.')
h3cVoPOTSEntityConfigSubLine = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 3, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigSubLine.setStatus('current')
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigSubLine.setDescription('This object indicates the voice subscriber line of this dial entity.')
h3cVoPOTSEntityConfigSendNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 31), ValueRangeConstraint(65534, 65534), ValueRangeConstraint(65535, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigSendNum.setStatus('current')
if mibBuilder.loadTexts: h3cVoPOTSEntityConfigSendNum.setDescription('This object indicates the digit of phone number to be sent to the destination. 0..31: Number of digits (that are extracted from the end of a number) to be sent, in the range of 0 to 31. It is not greater than the total number of digits of the called number. 65534: Sends all digits of a called number. 65535: Sends a truncated called number.')
h3cVoVoIPEntityConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 4), )
if mibBuilder.loadTexts: h3cVoVoIPEntityConfigTable.setStatus('current')
if mibBuilder.loadTexts: h3cVoVoIPEntityConfigTable.setDescription('This table contains the VoIP entity information.')
h3cVoVoIPEntityConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB", "h3cVoVoIPEntityCfgIndex"))
if mibBuilder.loadTexts: h3cVoVoIPEntityConfigEntry.setStatus('current')
if mibBuilder.loadTexts: h3cVoVoIPEntityConfigEntry.setDescription('The entry of h3cVoVoIPEntityConfigTable.')
h3cVoVoIPEntityCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoVoIPEntityCfgIndex.setStatus('current')
if mibBuilder.loadTexts: h3cVoVoIPEntityCfgIndex.setDescription('An arbitrary index that uniquely identifies a voice entity.')
h3cVoVoIPEntityCfgTargetType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("ras", 2), ("h323IpAddress", 3), ("sipIpAddress", 4), ("sipProxy", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPEntityCfgTargetType.setStatus('current')
if mibBuilder.loadTexts: h3cVoVoIPEntityCfgTargetType.setDescription('This object indicates the type of the session target of this entity.')
h3cVoVoIPEntityCfgTargetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 4, 1, 3), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPEntityCfgTargetAddrType.setStatus('current')
if mibBuilder.loadTexts: h3cVoVoIPEntityCfgTargetAddrType.setDescription('The IP address type of object h3cVoVoIPEntityCfgTargetAddr.')
h3cVoVoIPEntityCfgTargetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 4, 1, 4), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPEntityCfgTargetAddr.setStatus('current')
if mibBuilder.loadTexts: h3cVoVoIPEntityCfgTargetAddr.setDescription('This object indicates the target IP address.')
h3cVoEntityNumberTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5), )
if mibBuilder.loadTexts: h3cVoEntityNumberTable.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityNumberTable.setDescription('The table contains the number management information.')
h3cVoEntityNumberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB", "h3cVoEntityIndex"))
if mibBuilder.loadTexts: h3cVoEntityNumberEntry.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityNumberEntry.setDescription('The entry of h3cVoEntityNumberTable. H3cVoEntityIndex is used to uniquely identify these numbers registered on the server. The same value of h3cVoEntityIndex used in the corresponding H3CVoEntityCommonConfigTable is used here.')
h3cVoEntityNumberAuthUser = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityNumberAuthUser.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityNumberAuthUser.setDescription('This object indicates the username of the entity number to authorize.')
h3cVoEntityNumberPasswordType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityNumberPasswordType.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityNumberPasswordType.setDescription('This object indicates the password type of the entity number to authorize. The encrypting type of password: 0 : password simple, means password is clean text. 1 : password cipher, means password is encrypted text. default is 65535.')
h3cVoEntityNumberPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5, 1, 3), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 16), ValueSizeConstraint(24, 24), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoEntityNumberPassword.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityNumberPassword.setDescription('This object indicates the password of the entity number to authorize.')
h3cVoEntityNumberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5, 1, 4), H3cRegisterdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoEntityNumberStatus.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityNumberStatus.setDescription('This object indicates the current state of the entity number.')
h3cVoEntityNumberExpires = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 14, 1, 5, 1, 5), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoEntityNumberExpires.setStatus('current')
if mibBuilder.loadTexts: h3cVoEntityNumberExpires.setDescription('This is the interval time for entity number updating registered message.')
mibBuilder.exportSymbols("A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB", h3cVoEntityCfgFaxHRPackNum=h3cVoEntityCfgFaxHRPackNum, h3cVoVoIPEntityConfigEntry=h3cVoVoIPEntityConfigEntry, h3cVoEntityObjects=h3cVoEntityObjects, h3cVoEntityCreateTable=h3cVoEntityCreateTable, h3cVoEntityNumberAuthUser=h3cVoEntityNumberAuthUser, h3cVoVoIPEntityCfgTargetAddr=h3cVoVoIPEntityCfgTargetAddr, h3cVoVoIPEntityCfgTargetAddrType=h3cVoVoIPEntityCfgTargetAddrType, H3cFaxBaudrateType=H3cFaxBaudrateType, h3cVoEntityCfgFaxLevel=h3cVoEntityCfgFaxLevel, h3cVoEntityNumberEntry=h3cVoEntityNumberEntry, h3cVoEntityCreateEntry=h3cVoEntityCreateEntry, h3cVoEntityCfgVADEnable=h3cVoEntityCfgVADEnable, h3cVoPOTSEntityConfigTable=h3cVoPOTSEntityConfigTable, h3cVoPOTSEntityConfigIndex=h3cVoPOTSEntityConfigIndex, h3cVoEntityCfgDSCP=h3cVoEntityCfgDSCP, h3cVoEntityNumberStatus=h3cVoEntityNumberStatus, h3cVoEntityCfgCodec1st=h3cVoEntityCfgCodec1st, h3cVoVoIPEntityCfgTargetType=h3cVoVoIPEntityCfgTargetType, h3cVoEntityCfgPriority=h3cVoEntityCfgPriority, h3cVoEntityCfgCodec3rd=h3cVoEntityCfgCodec3rd, h3cVoPOTSEntityConfigPrefix=h3cVoPOTSEntityConfigPrefix, h3cVoVoIPEntityCfgIndex=h3cVoVoIPEntityCfgIndex, h3cVoPOTSEntityConfigEntry=h3cVoPOTSEntityConfigEntry, h3cVoEntityCommonConfigTable=h3cVoEntityCommonConfigTable, h3cVoEntityCfgFaxTrainMode=h3cVoEntityCfgFaxTrainMode, h3cVoEntityCfgFaxEcm=h3cVoEntityCfgFaxEcm, h3cVoEntityCfgCodec2nd=h3cVoEntityCfgCodec2nd, h3cVoEntityIndex=h3cVoEntityIndex, h3cVoPOTSEntityConfigSubLine=h3cVoPOTSEntityConfigSubLine, h3cVoEntityNumberPassword=h3cVoEntityNumberPassword, H3cFaxTrainMode=H3cFaxTrainMode, h3cVoEntityType=h3cVoEntityType, h3cVoEntityCfgFaxLocalTrainPara=h3cVoEntityCfgFaxLocalTrainPara, h3cVoEntityCfgDescription=h3cVoEntityCfgDescription, PYSNMP_MODULE_ID=h3cVoiceEntityControl, h3cVoEntityNumberPasswordType=h3cVoEntityNumberPasswordType, h3cVoEntityCfgIndex=h3cVoEntityCfgIndex, h3cVoPOTSEntityConfigSendNum=h3cVoPOTSEntityConfigSendNum, h3cVoEntityCfgFaxSendNSFEnable=h3cVoEntityCfgFaxSendNSFEnable, H3cRegisterdStatus=H3cRegisterdStatus, h3cVoEntityCfgFaxProtocol=h3cVoEntityCfgFaxProtocol, h3cVoVoIPEntityConfigTable=h3cVoVoIPEntityConfigTable, h3cVoEntityCfgOutbandMode=h3cVoEntityCfgOutbandMode, h3cVoEntityNumberTable=h3cVoEntityNumberTable, H3cOutBandMode=H3cOutBandMode, h3cVoEntityCfgCodec4th=h3cVoEntityCfgCodec4th, h3cVoEntityRowStatus=h3cVoEntityRowStatus, h3cVoEntityNumberExpires=h3cVoEntityNumberExpires, H3cCodecType=H3cCodecType, h3cVoEntityCommonConfigEntry=h3cVoEntityCommonConfigEntry, h3cVoEntityCfgFaxLRPackNum=h3cVoEntityCfgFaxLRPackNum, h3cVoiceEntityControl=h3cVoiceEntityControl, h3cVoEntityCfgFaxBaudrate=h3cVoEntityCfgFaxBaudrate, H3cFaxProtocolType=H3cFaxProtocolType)
