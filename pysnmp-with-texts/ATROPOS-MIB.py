#
# PySNMP MIB module ATROPOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATROPOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:31:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter64, Bits, MibIdentifier, IpAddress, Counter32, experimental, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, ObjectIdentity, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Bits", "MibIdentifier", "IpAddress", "Counter32", "experimental", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "ObjectIdentity", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atroposMIB = ModuleIdentity((1, 3, 6, 1, 3, 75, 4))
if mibBuilder.loadTexts: atroposMIB.setLastUpdated('9801010000Z')
if mibBuilder.loadTexts: atroposMIB.setOrganization('GE CRD')
if mibBuilder.loadTexts: atroposMIB.setContactInfo('Stephen F. Bush bushsf@crd.ge.com')
if mibBuilder.loadTexts: atroposMIB.setDescription('Experimental MIB modules for the Active Virtual Network Management Prediction (Atropos) system.')
lP = MibIdentifier((1, 3, 6, 1, 3, 75, 4, 1))
lPTable = MibTable((1, 3, 6, 1, 3, 75, 4, 1, 1), )
if mibBuilder.loadTexts: lPTable.setStatus('current')
if mibBuilder.loadTexts: lPTable.setDescription('Table of Atropos LP information.')
lPEntry = MibTableRow((1, 3, 6, 1, 3, 75, 4, 1, 1, 1), ).setIndexNames((0, "ATROPOS-MIB", "lPIndex"))
if mibBuilder.loadTexts: lPEntry.setStatus('current')
if mibBuilder.loadTexts: lPEntry.setDescription('Table of Atropos LP information.')
lPIndex = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: lPIndex.setStatus('current')
if mibBuilder.loadTexts: lPIndex.setDescription('The LP table index.')
lPID = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPID.setStatus('current')
if mibBuilder.loadTexts: lPID.setDescription('The LP identifier.')
lPLVT = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPLVT.setStatus('current')
if mibBuilder.loadTexts: lPLVT.setDescription('This is the LP Local Virtual Time.')
lPQRSize = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPQRSize.setStatus('current')
if mibBuilder.loadTexts: lPQRSize.setDescription('This is the LP Receive Queue Size.')
lPQSSize = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPQSSize.setStatus('current')
if mibBuilder.loadTexts: lPQSSize.setDescription('This is the LP send queue size.')
lPCausalityRollbacks = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPCausalityRollbacks.setStatus('current')
if mibBuilder.loadTexts: lPCausalityRollbacks.setDescription('This is the number of rollbacks this LP has suffered.')
lPToleranceRollbacks = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPToleranceRollbacks.setStatus('current')
if mibBuilder.loadTexts: lPToleranceRollbacks.setDescription('This is the number of rollbacks this LP has suffered.')
lPSQSize = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPSQSize.setStatus('current')
if mibBuilder.loadTexts: lPSQSize.setDescription('This is the LP state queue size.')
lPTolerance = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPTolerance.setStatus('current')
if mibBuilder.loadTexts: lPTolerance.setDescription("This is the allowable deviation between process's predicted state and the actual state.")
lPGVT = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPGVT.setStatus('current')
if mibBuilder.loadTexts: lPGVT.setDescription("This is this system's notion of Global Virtual Time.")
lPLookAhead = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPLookAhead.setStatus('current')
if mibBuilder.loadTexts: lPLookAhead.setDescription("This is this system's maximum time into which it can predict.")
lPGvtUpdate = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPGvtUpdate.setStatus('current')
if mibBuilder.loadTexts: lPGvtUpdate.setDescription('This is the GVT update rate.')
lPStepSize = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPStepSize.setStatus('current')
if mibBuilder.loadTexts: lPStepSize.setDescription('This is the lookahead (Delta) in milliseconds for each virtual message as generated from the driving process.')
lPReal = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPReal.setStatus('current')
if mibBuilder.loadTexts: lPReal.setDescription('This is the total number of real messages received.')
lPVirtual = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPVirtual.setStatus('current')
if mibBuilder.loadTexts: lPVirtual.setDescription('This is the total number of virtual messages received.')
lPNumPkts = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPNumPkts.setStatus('current')
if mibBuilder.loadTexts: lPNumPkts.setDescription('This is the total number of all Atropos packets received.')
lPNumAnti = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPNumAnti.setStatus('current')
if mibBuilder.loadTexts: lPNumAnti.setDescription('This is the total number of Anti-Messages transmitted by this Logical Process.')
lPPredAcc = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPPredAcc.setStatus('current')
if mibBuilder.loadTexts: lPPredAcc.setDescription('This is the prediction accuracy based upon time weighted average of the difference between predicted and real values.')
lPPropX = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPPropX.setStatus('current')
if mibBuilder.loadTexts: lPPropX.setDescription('This is the proportion of out-of-order messages received at this Logical Process.')
lPPropY = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPPropY.setStatus('current')
if mibBuilder.loadTexts: lPPropY.setDescription('This is the proportion of out-of-tolerance messages received at this Logical Process.')
lPETask = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPETask.setStatus('current')
if mibBuilder.loadTexts: lPETask.setDescription('This is the expected task execution wallclock time for this Logical Process.')
lPETrb = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPETrb.setStatus('current')
if mibBuilder.loadTexts: lPETrb.setDescription('This is the expected wallclock time spent performing a rollback for this Logical Process.')
lPVmRate = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPVmRate.setStatus('current')
if mibBuilder.loadTexts: lPVmRate.setDescription('This is the rate at which virtual messages were processed by this Logical Process.')
lPReRate = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPReRate.setStatus('current')
if mibBuilder.loadTexts: lPReRate.setDescription('This is the time until next virtual message.')
lPSpeedup = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPSpeedup.setStatus('current')
if mibBuilder.loadTexts: lPSpeedup.setDescription('This is the speedup, ratio of virtual time to wallclock time, of this logical process.')
lPLookahead = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 26), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPLookahead.setStatus('current')
if mibBuilder.loadTexts: lPLookahead.setDescription('This is the expected lookahead in milliseconds of this Logical Process.')
lPNumNoState = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPNumNoState.setStatus('current')
if mibBuilder.loadTexts: lPNumNoState.setDescription('This is the number of times there was no valid state to restore when needed by a rollback or when required to check prediction accuracy.')
lPStatePred = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 28), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPStatePred.setStatus('current')
if mibBuilder.loadTexts: lPStatePred.setDescription('This is the cached value of the state at the nearest time to the current time.')
lPPktPred = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 29), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPPktPred.setStatus('current')
if mibBuilder.loadTexts: lPPktPred.setDescription('This is the predicted value in a virtual message.')
lPTdiff = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 30), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPTdiff.setStatus('current')
if mibBuilder.loadTexts: lPTdiff.setDescription('This is the time difference between a predicted and an actual value.')
lPStateError = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 31), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPStateError.setStatus('current')
if mibBuilder.loadTexts: lPStateError.setDescription('This is the difference between the contents of an application value and the state value as seen within the virtual message.')
lPUptime = MibTableColumn((1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lPUptime.setStatus('current')
if mibBuilder.loadTexts: lPUptime.setDescription('This is the time in milliseconds that Atropos has been running on this node.')
mibBuilder.exportSymbols("ATROPOS-MIB", lPTolerance=lPTolerance, lPVirtual=lPVirtual, lPNumAnti=lPNumAnti, lPUptime=lPUptime, lPID=lPID, lPSQSize=lPSQSize, lPPropX=lPPropX, lPTdiff=lPTdiff, lPCausalityRollbacks=lPCausalityRollbacks, lPTable=lPTable, lPLookAhead=lPLookAhead, lPETrb=lPETrb, lPLookahead=lPLookahead, PYSNMP_MODULE_ID=atroposMIB, lPIndex=lPIndex, lPReRate=lPReRate, lPQSSize=lPQSSize, lPNumNoState=lPNumNoState, lP=lP, lPGVT=lPGVT, lPGvtUpdate=lPGvtUpdate, atroposMIB=atroposMIB, lPLVT=lPLVT, lPPredAcc=lPPredAcc, lPETask=lPETask, lPVmRate=lPVmRate, lPSpeedup=lPSpeedup, lPPktPred=lPPktPred, lPReal=lPReal, lPQRSize=lPQRSize, lPStatePred=lPStatePred, lPStepSize=lPStepSize, lPStateError=lPStateError, lPToleranceRollbacks=lPToleranceRollbacks, lPEntry=lPEntry, lPNumPkts=lPNumPkts, lPPropY=lPPropY)
