#
# PySNMP MIB module ATM-ADAPTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATM-ADAPTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("RFC1212", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, IpAddress, ObjectIdentity, MibIdentifier, Integer32, enterprises, NotificationType, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "IpAddress", "ObjectIdentity", "MibIdentifier", "Integer32", "enterprises", "NotificationType", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
atmAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29))
atmAdapterAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1))
atmAdapterMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 2))
atmfTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 1))
atmfTransmissionTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2))
atmfMediaTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3))
atmfTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 4))
atmfUnknownType = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 1))
atmfSonetSTS3c = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 2))
atmfDs3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 3))
atmf4B5B = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 4))
atmf8B10B = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 5))
atmfMediaUnknownType = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 1))
atmfMediaCoaxCable = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 2))
atmfMediaSingleMode = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 3))
atmfMediaMultiMode = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 4))
atmfMediaStp = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 5))
atmfMediaUtp = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 6))
atmfUnknownAdapterType = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 4, 1))
atmfTurbowaysATM_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 4, 2)).setLabel("atmfTurbowaysATM-100")
muxatmTrap = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxatmTrap.setStatus('mandatory')
muxatmString = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxatmString.setStatus('mandatory')
atmfAdapterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1))
atmfAtmLayerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2))
atmfAtmStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3))
atmfAdapterTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1), )
if mibBuilder.loadTexts: atmfAdapterTable.setStatus('mandatory')
atmfAdapterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1), ).setIndexNames((0, "ATM-ADAPTER-MIB", "atmfAdapterIndex"))
if mibBuilder.loadTexts: atmfAdapterEntry.setStatus('mandatory')
atmfAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterIndex.setStatus('mandatory')
atmfAdapterSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterSerialNumber.setStatus('mandatory')
atmfAdapterDiagVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterDiagVersion.setStatus('mandatory')
atmfAdapterSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterSoftwareVersion.setStatus('mandatory')
atmfAdapterTransmitBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9180))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterTransmitBufSize.setStatus('mandatory')
atmfAdapterReceiveBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9180))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterReceiveBufSize.setStatus('mandatory')
atmfAdapterTransmissionType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterTransmissionType.setStatus('mandatory')
atmfAdapterMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 8), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterMediaType.setStatus('mandatory')
atmfAdapterOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("inService", 2), ("outOfService", 3), ("loopBack", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterOperStatus.setStatus('mandatory')
atmfAdapterType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 10), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterType.setStatus('mandatory')
atmfAtmLayerTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1), )
if mibBuilder.loadTexts: atmfAtmLayerTable.setStatus('mandatory')
atmfAtmLayerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1), ).setIndexNames((0, "ATM-ADAPTER-MIB", "atmfAtmLayerIndex"))
if mibBuilder.loadTexts: atmfAtmLayerEntry.setStatus('mandatory')
atmfAtmLayerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerIndex.setStatus('mandatory')
atmfAtmLayerMaxVPCs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerMaxVPCs.setStatus('mandatory')
atmfAtmLayerMaxVCCs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerMaxVCCs.setStatus('mandatory')
atmfAtmLayerConfiguredVPCs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerConfiguredVPCs.setStatus('mandatory')
atmfAtmLayerConfiguredVCCs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerConfiguredVCCs.setStatus('mandatory')
atmfAtmLayerMaxVpiBits = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerMaxVpiBits.setStatus('mandatory')
atmfAtmLayerMaxVciBits = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerMaxVciBits.setStatus('mandatory')
atmfAtmLayerUniType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("public", 1), ("private", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerUniType.setStatus('mandatory')
atmfAtmStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1), )
if mibBuilder.loadTexts: atmfAtmStatsTable.setStatus('mandatory')
atmfAtmStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1), ).setIndexNames((0, "ATM-ADAPTER-MIB", "atmfAtmStatsIndex"))
if mibBuilder.loadTexts: atmfAtmStatsEntry.setStatus('mandatory')
atmfAtmStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmStatsIndex.setStatus('mandatory')
atmfAtmStatsReceivedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmStatsReceivedCells.setStatus('mandatory')
atmfAtmStatsDroppedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmStatsDroppedPackets.setStatus('mandatory')
atmfAtmStatsTransmittedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmStatsTransmittedCells.setStatus('mandatory')
mibBuilder.exportSymbols("ATM-ADAPTER-MIB", atmfAtmStatsReceivedCells=atmfAtmStatsReceivedCells, atmfAtmStatsTransmittedCells=atmfAtmStatsTransmittedCells, atmfAdapterIndex=atmfAdapterIndex, atmfAtmLayerTable=atmfAtmLayerTable, muxatmTrap=muxatmTrap, atmfUnknownAdapterType=atmfUnknownAdapterType, atmfAdapterEntry=atmfAdapterEntry, atmfAdapterSerialNumber=atmfAdapterSerialNumber, atmfAtmLayerMaxVpiBits=atmfAtmLayerMaxVpiBits, atmf4B5B=atmf4B5B, atmfAdapterReceiveBufSize=atmfAdapterReceiveBufSize, atmfAdapterGroup=atmfAdapterGroup, atmfAtmLayerGroup=atmfAtmLayerGroup, atmfMediaSingleMode=atmfMediaSingleMode, atmfAtmLayerIndex=atmfAtmLayerIndex, atmfAtmStatsDroppedPackets=atmfAtmStatsDroppedPackets, atmfTurbowaysATM_100=atmfTurbowaysATM_100, atmfAtmStatsGroup=atmfAtmStatsGroup, atmfUnknownType=atmfUnknownType, atmfAdapterTransmitBufSize=atmfAdapterTransmitBufSize, atmfAtmLayerEntry=atmfAtmLayerEntry, atmfAtmLayerMaxVCCs=atmfAtmLayerMaxVCCs, atmfAtmLayerConfiguredVCCs=atmfAtmLayerConfiguredVCCs, atmfMediaMultiMode=atmfMediaMultiMode, atmfAdapterDiagVersion=atmfAdapterDiagVersion, atmfMediaUtp=atmfMediaUtp, atmfMediaTypes=atmfMediaTypes, atmfAdapterTransmissionType=atmfAdapterTransmissionType, atmfAtmStatsIndex=atmfAtmStatsIndex, atmfAtmLayerMaxVPCs=atmfAtmLayerMaxVPCs, atmfTrap=atmfTrap, atmfAdapterOperStatus=atmfAdapterOperStatus, atmfTransmissionTypes=atmfTransmissionTypes, atmfAtmStatsTable=atmfAtmStatsTable, atmfAdapterSoftwareVersion=atmfAdapterSoftwareVersion, atmfMediaUnknownType=atmfMediaUnknownType, atmfAdapterType=atmfAdapterType, atmAdapterAdmin=atmAdapterAdmin, atmfAtmLayerMaxVciBits=atmfAtmLayerMaxVciBits, atmf8B10B=atmf8B10B, atmfTypes=atmfTypes, atmfAdapterTable=atmfAdapterTable, ibm=ibm, atmfSonetSTS3c=atmfSonetSTS3c, atmfAtmStatsEntry=atmfAtmStatsEntry, atmAdapter=atmAdapter, atmfMediaStp=atmfMediaStp, atmfAtmLayerConfiguredVPCs=atmfAtmLayerConfiguredVPCs, atmfDs3=atmfDs3, atmfAtmLayerUniType=atmfAtmLayerUniType, atmfAdapterMediaType=atmfAdapterMediaType, atmAdapterMib=atmAdapterMib, muxatmString=muxatmString, atmfMediaCoaxCable=atmfMediaCoaxCable, ibmProd=ibmProd)
