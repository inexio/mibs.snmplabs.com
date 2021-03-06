#
# PySNMP MIB module ASCEND-MIBATMQOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBATMQOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, ModuleIdentity, TimeTicks, Unsigned32, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, ObjectIdentity, Counter32, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "ModuleIdentity", "TimeTicks", "Unsigned32", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "ObjectIdentity", "Counter32", "Bits", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibatmQosProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 21))
mibatmQosProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 21, 1), )
if mibBuilder.loadTexts: mibatmQosProfileTable.setStatus('mandatory')
mibatmQosProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1), ).setIndexNames((0, "ASCEND-MIBATMQOS-MIB", "atmQosProfile-ContractName"))
if mibBuilder.loadTexts: mibatmQosProfileEntry.setStatus('mandatory')
atmQosProfile_ContractName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 1), DisplayString()).setLabel("atmQosProfile-ContractName").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmQosProfile_ContractName.setStatus('mandatory')
atmQosProfile_TrafficDescriptorIndex = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 2), Integer32()).setLabel("atmQosProfile-TrafficDescriptorIndex").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmQosProfile_TrafficDescriptorIndex.setStatus('mandatory')
atmQosProfile_TrafficDescriptorType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(17, 3, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("unknownTrafficDescr", 17), ("noclpNoscr", 3), ("noclpScr", 6), ("clpNotaggingScr", 7), ("clpTaggingScr", 8), ("clpTransparentNoscr", 10), ("clpTransparentScr", 11), ("noclpTaggingNoscr", 12), ("noclpNoscrCdvt", 13), ("noclpScrCdvt", 14), ("clpNotaggingScrCdvt", 15), ("clpTaggingScrCdvt", 16)))).setLabel("atmQosProfile-TrafficDescriptorType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_TrafficDescriptorType.setStatus('mandatory')
atmQosProfile_AtmServiceCategory = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("cbr", 1), ("realTimeVbr", 2), ("nonRealTimeVbr", 3), ("ubr", 4)))).setLabel("atmQosProfile-AtmServiceCategory").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_AtmServiceCategory.setStatus('mandatory')
atmQosProfile_PeakRateKbitsPerSec = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 6), Integer32()).setLabel("atmQosProfile-PeakRateKbitsPerSec").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_PeakRateKbitsPerSec.setStatus('mandatory')
atmQosProfile_PeakCellRateCellsPerSec = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 7), Integer32()).setLabel("atmQosProfile-PeakCellRateCellsPerSec").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_PeakCellRateCellsPerSec.setStatus('mandatory')
atmQosProfile_SustainableRateKbitsPerSec = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 9), Integer32()).setLabel("atmQosProfile-SustainableRateKbitsPerSec").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_SustainableRateKbitsPerSec.setStatus('mandatory')
atmQosProfile_SustainableCellRateCellsPerSec = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 10), Integer32()).setLabel("atmQosProfile-SustainableCellRateCellsPerSec").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_SustainableCellRateCellsPerSec.setStatus('mandatory')
atmQosProfile_IgnoreCellDelayVariationTolerance = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("atmQosProfile-IgnoreCellDelayVariationTolerance").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_IgnoreCellDelayVariationTolerance.setStatus('mandatory')
atmQosProfile_CellDelayVariationTolerance = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 12), Integer32()).setLabel("atmQosProfile-CellDelayVariationTolerance").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_CellDelayVariationTolerance.setStatus('mandatory')
atmQosProfile_IgnoreMaxBurstSize = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("atmQosProfile-IgnoreMaxBurstSize").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_IgnoreMaxBurstSize.setStatus('mandatory')
atmQosProfile_MaxBurstSize = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 14), Integer32()).setLabel("atmQosProfile-MaxBurstSize").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_MaxBurstSize.setStatus('mandatory')
atmQosProfile_AalType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("aal0", 1), ("aal5", 2), ("unspecified", 3)))).setLabel("atmQosProfile-AalType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_AalType.setStatus('mandatory')
atmQosProfile_EarlyPacketDiscard = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("atmQosProfile-EarlyPacketDiscard").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_EarlyPacketDiscard.setStatus('mandatory')
atmQosProfile_PartialPacketDiscard = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("atmQosProfile-PartialPacketDiscard").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_PartialPacketDiscard.setStatus('mandatory')
atmQosProfile_TagOrDiscard = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tag", 1), ("discard", 2)))).setLabel("atmQosProfile-TagOrDiscard").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_TagOrDiscard.setStatus('mandatory')
atmQosProfile_SubChannel = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 21), Integer32()).setLabel("atmQosProfile-SubChannel").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_SubChannel.setStatus('mandatory')
atmQosProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("atmQosProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmQosProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBATMQOS-MIB", atmQosProfile_TagOrDiscard=atmQosProfile_TagOrDiscard, atmQosProfile_PeakRateKbitsPerSec=atmQosProfile_PeakRateKbitsPerSec, mibatmQosProfileEntry=mibatmQosProfileEntry, atmQosProfile_Action_o=atmQosProfile_Action_o, mibatmQosProfile=mibatmQosProfile, atmQosProfile_SubChannel=atmQosProfile_SubChannel, atmQosProfile_PartialPacketDiscard=atmQosProfile_PartialPacketDiscard, mibatmQosProfileTable=mibatmQosProfileTable, atmQosProfile_AtmServiceCategory=atmQosProfile_AtmServiceCategory, DisplayString=DisplayString, atmQosProfile_ContractName=atmQosProfile_ContractName, atmQosProfile_IgnoreCellDelayVariationTolerance=atmQosProfile_IgnoreCellDelayVariationTolerance, atmQosProfile_SustainableRateKbitsPerSec=atmQosProfile_SustainableRateKbitsPerSec, atmQosProfile_MaxBurstSize=atmQosProfile_MaxBurstSize, atmQosProfile_IgnoreMaxBurstSize=atmQosProfile_IgnoreMaxBurstSize, atmQosProfile_EarlyPacketDiscard=atmQosProfile_EarlyPacketDiscard, atmQosProfile_CellDelayVariationTolerance=atmQosProfile_CellDelayVariationTolerance, atmQosProfile_PeakCellRateCellsPerSec=atmQosProfile_PeakCellRateCellsPerSec, atmQosProfile_TrafficDescriptorIndex=atmQosProfile_TrafficDescriptorIndex, atmQosProfile_AalType=atmQosProfile_AalType, atmQosProfile_TrafficDescriptorType=atmQosProfile_TrafficDescriptorType, atmQosProfile_SustainableCellRateCellsPerSec=atmQosProfile_SustainableCellRateCellsPerSec)
