#
# PySNMP MIB module MERU-CONFIG-PACKETCAPTURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-CONFIG-PACKETCAPTURE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:11:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
MwlEncapsulationType, MwlRateLimitMode, MwlOnOffSwitch, MwlPacketCaptureMode, MwlRxTxOption, MwlEnableDisableOption = mibBuilder.importSymbols("MERU-TC", "MwlEncapsulationType", "MwlRateLimitMode", "MwlOnOffSwitch", "MwlPacketCaptureMode", "MwlRxTxOption", "MwlEnableDisableOption")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, IpAddress, Integer32, MibIdentifier, enterprises, NotificationType, Gauge32, Counter32, Counter64, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "IpAddress", "Integer32", "MibIdentifier", "enterprises", "NotificationType", "Gauge32", "Counter32", "Counter64", "ObjectIdentity", "Unsigned32")
TextualConvention, TruthValue, TimeStamp, MacAddress, RowStatus, DisplayString, DateAndTime, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "TimeStamp", "MacAddress", "RowStatus", "DisplayString", "DateAndTime", "TimeInterval")
mwConfigPacketCapture = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17))
if mibBuilder.loadTexts: mwConfigPacketCapture.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigPacketCapture.setOrganization('Meru Networks')
if mibBuilder.loadTexts: mwConfigPacketCapture.setContactInfo('support@merunetworks.com')
if mibBuilder.loadTexts: mwConfigPacketCapture.setDescription('This MIB defines all the managed objects used to manage the Meru WLAN Packet Capture Configuration infrastructure')
mwPacketCaptureProfileTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1), )
if mibBuilder.loadTexts: mwPacketCaptureProfileTable.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileTable.setDescription('This object describes AP Packet Capture ')
mwPacketCaptureProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1), ).setIndexNames((0, "MERU-CONFIG-PACKETCAPTURE-MIB", "mwPacketCaptureProfileTableIndex"))
if mibBuilder.loadTexts: mwPacketCaptureProfileEntry.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileEntry.setDescription('This object describes AP Packet Capture ')
mwPacketCaptureProfileTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: mwPacketCaptureProfileTableIndex.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileTableIndex.setDescription('The index value of the table ')
mwPacketCaptureProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileName.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileName.setDescription('This object describes Profile Name')
mwPacketCaptureProfileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 3), MwlEnableDisableOption()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileStatus.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileStatus.setDescription('This object describes Enable/Disable')
mwPacketCaptureProfileConnectivityMode = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 4), MwlPacketCaptureMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileConnectivityMode.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileConnectivityMode.setDescription('This object describes L2/L3 Mode')
mwPacketCaptureProfileDestinationIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileDestinationIp.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileDestinationIp.setDescription('This object describes Destination IP Address')
mwPacketCaptureProfileUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileUDPPort.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileUDPPort.setDescription('This object describes UDP Destination Port')
mwPacketCaptureProfileDestinationMac = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 7), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileDestinationMac.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileDestinationMac.setDescription('This object describes Destination MAC for L2 Mode')
mwPacketCaptureProfileRxTx = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 8), MwlRxTxOption()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPacketCaptureProfileRxTx.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileRxTx.setDescription('This object describes Rx only/Tx only/Both')
mwPacketCaptureProfileRateLimitMode = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 9), MwlRateLimitMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileRateLimitMode.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileRateLimitMode.setDescription('This object describes Rate Limiting per station or cumulative')
mwPacketCaptureProfileTokenBucketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileTokenBucketRate.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileTokenBucketRate.setDescription('This object describes Token Bucket Rate')
mwPacketCaptureProfileTokenBucketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 11), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileTokenBucketSize.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileTokenBucketSize.setDescription('This object describes Token Bucket Size')
mwPacketCaptureProfileApList = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileApList.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileApList.setDescription('This object describes AP Selection (ID)')
mwPacketCaptureProfileFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileFilter.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileFilter.setDescription('This object describes Extended Filter String')
mwPacketCaptureProfileInterfaceList = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileInterfaceList.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileInterfaceList.setDescription('This object describes Interface Index')
mwPacketCaptureProfilePacketTruncationLength = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 15), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfilePacketTruncationLength.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfilePacketTruncationLength.setDescription('This object describes Packet Truncation Length')
mwPacketCaptureProfileRateLimiting = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 16), MwlOnOffSwitch()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileRateLimiting.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileRateLimiting.setDescription('This object describes Rate Limiting')
mwPacketCaptureProfileCaptureSiblingFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 17), MwlOnOffSwitch()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileCaptureSiblingFrames.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileCaptureSiblingFrames.setDescription('This object describes Capture Sibling Frames')
mwPacketCaptureProfileEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 18), MwlEncapsulationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileEncapsulation.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileEncapsulation.setDescription('This object describes Encapsulation')
mwPacketCaptureProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 19), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileRowStatus.setStatus('current')
if mibBuilder.loadTexts: mwPacketCaptureProfileRowStatus.setDescription('This object is used to create and delete rows in the table')
mibBuilder.exportSymbols("MERU-CONFIG-PACKETCAPTURE-MIB", mwPacketCaptureProfileEntry=mwPacketCaptureProfileEntry, mwPacketCaptureProfileRateLimitMode=mwPacketCaptureProfileRateLimitMode, mwPacketCaptureProfileApList=mwPacketCaptureProfileApList, mwPacketCaptureProfileDestinationIp=mwPacketCaptureProfileDestinationIp, mwPacketCaptureProfileTokenBucketSize=mwPacketCaptureProfileTokenBucketSize, mwPacketCaptureProfileStatus=mwPacketCaptureProfileStatus, mwPacketCaptureProfilePacketTruncationLength=mwPacketCaptureProfilePacketTruncationLength, mwPacketCaptureProfileInterfaceList=mwPacketCaptureProfileInterfaceList, mwConfigPacketCapture=mwConfigPacketCapture, mwPacketCaptureProfileRxTx=mwPacketCaptureProfileRxTx, mwPacketCaptureProfileRateLimiting=mwPacketCaptureProfileRateLimiting, mwPacketCaptureProfileCaptureSiblingFrames=mwPacketCaptureProfileCaptureSiblingFrames, mwPacketCaptureProfileDestinationMac=mwPacketCaptureProfileDestinationMac, mwPacketCaptureProfileTable=mwPacketCaptureProfileTable, mwPacketCaptureProfileName=mwPacketCaptureProfileName, mwPacketCaptureProfileFilter=mwPacketCaptureProfileFilter, mwPacketCaptureProfileUDPPort=mwPacketCaptureProfileUDPPort, mwPacketCaptureProfileRowStatus=mwPacketCaptureProfileRowStatus, mwPacketCaptureProfileTableIndex=mwPacketCaptureProfileTableIndex, mwPacketCaptureProfileTokenBucketRate=mwPacketCaptureProfileTokenBucketRate, mwPacketCaptureProfileConnectivityMode=mwPacketCaptureProfileConnectivityMode, PYSNMP_MODULE_ID=mwConfigPacketCapture, mwPacketCaptureProfileEncapsulation=mwPacketCaptureProfileEncapsulation)