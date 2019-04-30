#
# PySNMP MIB module MICOM-TRAFFIC-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MICOM-TRAFFIC-MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:02:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
micom_oscar, = mibBuilder.importSymbols("MICOM-OSCAR-MIB", "micom-oscar")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Integer32, TimeTicks, iso, Counter32, Bits, NotificationType, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Integer32", "TimeTicks", "iso", "Counter32", "Bits", "NotificationType", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
micom_2tm = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 27)).setLabel("micom-2tm")
tm2_configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1)).setLabel("tm2-configuration")
tm2_status = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2)).setLabel("tm2-status")
tm2_statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3)).setLabel("tm2-statistics")
tm2_control = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4)).setLabel("tm2-control")
mcmTMclassParamTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1), )
if mibBuilder.loadTexts: mcmTMclassParamTable.setStatus('mandatory')
mcmTMclassParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1), ).setIndexNames((0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassParamSccNum"), (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassParamFRDlciNum"), (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassParamMPANLDlciNum"))
if mibBuilder.loadTexts: mcmTMclassParamEntry.setStatus('mandatory')
mcmTMclassParamSccNum = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassParamSccNum.setStatus('mandatory')
mcmTMclassParamFRDlciNum = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1007))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassParamFRDlciNum.setStatus('mandatory')
mcmTMclassParamMPANLDlciNum = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(65535, 65535), ValueRangeConstraint(0, 1024), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassParamMPANLDlciNum.setStatus('mandatory')
mcmTMclassParamPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassParamPriority.setStatus('mandatory')
mcmTMclassParamCIR = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassParamCIR.setStatus('mandatory')
mcmTMclassParamExcessInfoRate = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassParamExcessInfoRate.setStatus('mandatory')
mcmTMclassParamMaxBurstBytesSz = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassParamMaxBurstBytesSz.setStatus('mandatory')
mcmTMclassParamMaxBurstFrmSz = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassParamMaxBurstFrmSz.setStatus('mandatory')
mcmTMclassParamAvgPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1536))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassParamAvgPacketSize.setStatus('mandatory')
mcmTMclassParamMaxPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1536))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassParamMaxPacketSize.setStatus('mandatory')
mcmTMclassParamDelta = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassParamDelta.setStatus('mandatory')
mcmTMclassParamSFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassParamSFrames.setStatus('mandatory')
mcmTMGlobalParamGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 2))
mcmTmRateEnforcement = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTmRateEnforcement.setStatus('mandatory')
mcmTmLineEfficiency = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTmLineEfficiency.setStatus('mandatory')
mcmTmWeightedRoundRobin = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTmWeightedRoundRobin.setStatus('mandatory')
nvmTMGlobalParamGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 3))
nvmTmRateEnforcement = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmTmRateEnforcement.setStatus('mandatory')
nvmTmLineEfficiency = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmTmLineEfficiency.setStatus('mandatory')
nvmTmWeightedRoundRobin = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmTmWeightedRoundRobin.setStatus('mandatory')
mcmTMclassStateTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1), )
if mibBuilder.loadTexts: mcmTMclassStateTable.setStatus('mandatory')
mcmTMclassStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1), ).setIndexNames((0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassStateSccNum"), (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassStateFRDlciNum"), (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassStateMPANLDlciNum"))
if mibBuilder.loadTexts: mcmTMclassStateEntry.setStatus('mandatory')
mcmTMclassStateSccNum = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStateSccNum.setStatus('mandatory')
mcmTMclassStateFRDlciNum = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1007))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStateFRDlciNum.setStatus('mandatory')
mcmTMclassStateMPANLDlciNum = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(65535, 65535), ValueRangeConstraint(0, 1024), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStateMPANLDlciNum.setStatus('mandatory')
mcmTMclassStateCurrentInfoRate = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStateCurrentInfoRate.setStatus('mandatory')
mcmTMclassStateMinInfoRate = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStateMinInfoRate.setStatus('mandatory')
mcmTMclassStateAvgTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStateAvgTxRate.setStatus('mandatory')
mcmTMclassStateBytesQueued = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStateBytesQueued.setStatus('mandatory')
mcmTMclassStateFramesQueued = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStateFramesQueued.setStatus('mandatory')
mcmTMclassStatsTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1), )
if mibBuilder.loadTexts: mcmTMclassStatsTable.setStatus('mandatory')
mcmTMclassStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1), ).setIndexNames((0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassStatsSccNum"), (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassStatsFRDlciNum"), (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassStatsMPANLDlciNum"))
if mibBuilder.loadTexts: mcmTMclassStatsEntry.setStatus('mandatory')
mcmTMclassStatsSccNum = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsSccNum.setStatus('mandatory')
mcmTMclassStatsFRDlciNum = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1007))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsFRDlciNum.setStatus('mandatory')
mcmTMclassStatsMPANLDlciNum = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(65535, 65535), ValueRangeConstraint(0, 1024), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsMPANLDlciNum.setStatus('mandatory')
mcmTMclassStatsTotalBytesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsTotalBytesTx.setStatus('mandatory')
mcmTMclassStatsTotalFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsTotalFramesTx.setStatus('mandatory')
mcmTMclassStatsTotalFragsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsTotalFragsTx.setStatus('mandatory')
mcmTMclassStatsTotalBytesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsTotalBytesRx.setStatus('mandatory')
mcmTMclassStatsTotalFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsTotalFramesRx.setStatus('mandatory')
mcmTMclassStatsTotalFragsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsTotalFragsRx.setStatus('mandatory')
mcmTMclassStatsPktsDiscQueFull = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsPktsDiscQueFull.setStatus('mandatory')
mcmTMclassStatsPktsDiscQueOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsPktsDiscQueOverflow.setStatus('mandatory')
mcmTMclassStatsPktsDiscEmitFail = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsPktsDiscEmitFail.setStatus('mandatory')
mcmTMclassStatsPktsDiscEmitQueFull = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsPktsDiscEmitQueFull.setStatus('mandatory')
mcmTMclassStatsTotalFecnClearRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsTotalFecnClearRcvd.setStatus('mandatory')
mcmTMclassStatsTotalFecnSetRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsTotalFecnSetRcvd.setStatus('mandatory')
mcmTMclassStatsTotalBecnRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMclassStatsTotalBecnRcvd.setStatus('mandatory')
mcmTMcntlCounterTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4, 1), )
if mibBuilder.loadTexts: mcmTMcntlCounterTable.setStatus('obsolete')
mcmTMcntlCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4, 1, 1), ).setIndexNames((0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMcntlCounterSccNum"), (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMcntlCounterFRDlciNum"), (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMcntlCounterMPANLDlciNum"))
if mibBuilder.loadTexts: mcmTMcntlCounterEntry.setStatus('obsolete')
mcmTMcntlCounterSccNum = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMcntlCounterSccNum.setStatus('obsolete')
mcmTMcntlCounterFRDlciNum = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1007))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMcntlCounterFRDlciNum.setStatus('obsolete')
mcmTMcntlCounterMPANLDlciNum = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmTMcntlCounterMPANLDlciNum.setStatus('obsolete')
mcmTMcntlCounterClassStatsReset = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: mcmTMcntlCounterClassStatsReset.setStatus('obsolete')
mibBuilder.exportSymbols("MICOM-TRAFFIC-MGMT-MIB", mcmTMclassStateSccNum=mcmTMclassStateSccNum, nvmTmLineEfficiency=nvmTmLineEfficiency, mcmTMclassParamFRDlciNum=mcmTMclassParamFRDlciNum, mcmTMclassStateBytesQueued=mcmTMclassStateBytesQueued, mcmTMclassParamSFrames=mcmTMclassParamSFrames, mcmTMclassParamExcessInfoRate=mcmTMclassParamExcessInfoRate, mcmTMclassStatsSccNum=mcmTMclassStatsSccNum, mcmTMclassStateEntry=mcmTMclassStateEntry, mcmTMclassParamMPANLDlciNum=mcmTMclassParamMPANLDlciNum, mcmTMclassParamDelta=mcmTMclassParamDelta, mcmTMclassStateCurrentInfoRate=mcmTMclassStateCurrentInfoRate, mcmTMclassParamMaxBurstFrmSz=mcmTMclassParamMaxBurstFrmSz, mcmTMclassStatsTotalFramesTx=mcmTMclassStatsTotalFramesTx, mcmTMclassStatsPktsDiscQueOverflow=mcmTMclassStatsPktsDiscQueOverflow, mcmTMcntlCounterMPANLDlciNum=mcmTMcntlCounterMPANLDlciNum, mcmTmLineEfficiency=mcmTmLineEfficiency, mcmTMclassParamSccNum=mcmTMclassParamSccNum, tm2_status=tm2_status, mcmTMclassParamPriority=mcmTMclassParamPriority, mcmTMclassParamCIR=mcmTMclassParamCIR, mcmTMclassParamTable=mcmTMclassParamTable, mcmTMclassStateMPANLDlciNum=mcmTMclassStateMPANLDlciNum, mcmTMclassStatsPktsDiscEmitFail=mcmTMclassStatsPktsDiscEmitFail, mcmTMGlobalParamGroup=mcmTMGlobalParamGroup, nvmTmRateEnforcement=nvmTmRateEnforcement, tm2_control=tm2_control, mcmTMcntlCounterEntry=mcmTMcntlCounterEntry, nvmTMGlobalParamGroup=nvmTMGlobalParamGroup, tm2_configuration=tm2_configuration, mcmTMclassStatsTotalFramesRx=mcmTMclassStatsTotalFramesRx, mcmTMclassParamAvgPacketSize=mcmTMclassParamAvgPacketSize, mcmTMclassParamMaxPacketSize=mcmTMclassParamMaxPacketSize, mcmTMclassParamEntry=mcmTMclassParamEntry, nvmTmWeightedRoundRobin=nvmTmWeightedRoundRobin, mcmTMclassStateMinInfoRate=mcmTMclassStateMinInfoRate, mcmTMclassStateFramesQueued=mcmTMclassStateFramesQueued, micom_2tm=micom_2tm, mcmTMclassStatsTable=mcmTMclassStatsTable, mcmTMclassStatsPktsDiscEmitQueFull=mcmTMclassStatsPktsDiscEmitQueFull, mcmTMcntlCounterTable=mcmTMcntlCounterTable, mcmTmWeightedRoundRobin=mcmTmWeightedRoundRobin, mcmTMcntlCounterClassStatsReset=mcmTMcntlCounterClassStatsReset, mcmTMcntlCounterFRDlciNum=mcmTMcntlCounterFRDlciNum, mcmTMclassStatsTotalFecnClearRcvd=mcmTMclassStatsTotalFecnClearRcvd, mcmTMclassStateTable=mcmTMclassStateTable, mcmTMclassStateFRDlciNum=mcmTMclassStateFRDlciNum, mcmTMclassStatsFRDlciNum=mcmTMclassStatsFRDlciNum, mcmTMclassParamMaxBurstBytesSz=mcmTMclassParamMaxBurstBytesSz, tm2_statistics=tm2_statistics, mcmTMclassStateAvgTxRate=mcmTMclassStateAvgTxRate, mcmTMclassStatsTotalFragsRx=mcmTMclassStatsTotalFragsRx, mcmTMclassStatsEntry=mcmTMclassStatsEntry, mcmTMcntlCounterSccNum=mcmTMcntlCounterSccNum, mcmTMclassStatsTotalFecnSetRcvd=mcmTMclassStatsTotalFecnSetRcvd, mcmTMclassStatsTotalBytesTx=mcmTMclassStatsTotalBytesTx, mcmTMclassStatsTotalBytesRx=mcmTMclassStatsTotalBytesRx, mcmTMclassStatsTotalBecnRcvd=mcmTMclassStatsTotalBecnRcvd, mcmTMclassStatsTotalFragsTx=mcmTMclassStatsTotalFragsTx, mcmTMclassStatsPktsDiscQueFull=mcmTMclassStatsPktsDiscQueFull, mcmTmRateEnforcement=mcmTmRateEnforcement, mcmTMclassStatsMPANLDlciNum=mcmTMclassStatsMPANLDlciNum)