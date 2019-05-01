#
# PySNMP MIB module BOUNDARY-ACCESSS-NODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BOUNDARY-ACCESSS-NODE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:40:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, Bits, IpAddress, Counter32, Gauge32, ObjectIdentity, iso, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, ModuleIdentity, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Bits", "IpAddress", "Counter32", "Gauge32", "ObjectIdentity", "iso", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibmBANMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12))
ibmBANTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1), )
if mibBuilder.loadTexts: ibmBANTable.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANTable.setDescription('A table of information related to bridge ports configured for Boundary Access Node capability.')
ibmBANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1), ).setIndexNames((0, "BOUNDARY-ACCESSS-NODE-MIB", "ibmBANbridgePort"))
if mibBuilder.loadTexts: ibmBANEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANEntry.setDescription('Statistics, status and configuration information on a specific Boundary Access Node port.')
ibmBANbridgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ibmBANbridgePort.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANbridgePort.setDescription('The BAN bridge port number. It is the same value as the bridge MIBs dot1dBasePort.')
ibmBANifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANifIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANifIndex.setDescription('The interface index identifying the physical interface this bridge port is assicated with. It is the same value as mib-2 ifIndex.')
ibmBANDLCImacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANDLCImacAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANDLCImacAddress.setDescription('The MAC address of the frame relay DLCI.')
ibmBANboundaryNodeID = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANboundaryNodeID.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANboundaryNodeID.setDescription('The boundary node identifier for the SNA node.')
ibmBANtype = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bridged", 1), ("dlswTerminated", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANtype.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANtype.setDescription('An indication whether this port is bridged or DLSw terminated.')
ibmBANstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("initFail", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANstatus.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANstatus.setDescription('The status of the ban port with the following values: up(1) - FR DLCI up and running as intended down(2) - FR DLCI is not running initFail(3) - A configuration problem exists')
ibmBANinIFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinIFrames.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinIFrames.setDescription('Count of received I-frames.')
ibmBANinRRs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinRRs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinRRs.setDescription('Count of received RRs.')
ibmBANinRNRs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinRNRs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinRNRs.setDescription('Count of received RNRs.')
ibmBANinRejs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinRejs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinRejs.setDescription('Count of received frame rejects.')
ibmBANinTests = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinTests.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinTests.setDescription('Count of received TESTs.')
ibmBANinTestRsps = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinTestRsps.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinTestRsps.setDescription('Count of received TEST responses.')
ibmBANinXIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinXIDs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinXIDs.setDescription('Count of received XIDs.')
ibmBANinXIDRsps = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinXIDRsps.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinXIDRsps.setDescription('Count of received XID responses.')
ibmBANinSABMEs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinSABMEs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinSABMEs.setDescription('Count of received SABMEs.')
ibmBANinUAs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinUAs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinUAs.setDescription('Count of received UAs.')
ibmBANinDMs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinDMs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinDMs.setDescription('Count of received DMs.')
ibmBANinDISCs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinDISCs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinDISCs.setDescription('Count of received DISCs.')
ibmBANinFRMRs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinFRMRs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinFRMRs.setDescription('Count of received FRMRs.')
ibmBANinOthers = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANinOthers.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANinOthers.setDescription('Count of other packets not counted by the other incoming counters.')
ibmBANoutIFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutIFrames.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutIFrames.setDescription('Count of transmitted I-frames.')
ibmBANoutRRs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutRRs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutRRs.setDescription('Count of transmitted RRs.')
ibmBANoutRNRs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutRNRs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutRNRs.setDescription('Count of transmitted RNRs.')
ibmBANoutRejs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutRejs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutRejs.setDescription('Count of transmitted frame rejects.')
ibmBANoutTests = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutTests.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutTests.setDescription('Count of transmitted TESTs.')
ibmBANoutTestRsps = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutTestRsps.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutTestRsps.setDescription('Count of transmitted TEST responses.')
ibmBANoutXIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutXIDs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutXIDs.setDescription('Count of transmitted XIDs.')
ibmBANoutXIDRsps = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutXIDRsps.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutXIDRsps.setDescription('Count of transmitted XID responses.')
ibmBANoutSABMEs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutSABMEs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutSABMEs.setDescription('Count of transmitted SABMEs.')
ibmBANoutUAs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutUAs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutUAs.setDescription('Count of transmitted UAs.')
ibmBANoutDMs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutDMs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutDMs.setDescription('Count of transmitted DMs.')
ibmBANoutDISCs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutDISCs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutDISCs.setDescription('Count of transmitted DISCs.')
ibmBANoutFRMRs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutFRMRs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutFRMRs.setDescription('Count of transmitted FRMRs.')
ibmBANoutOthers = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBANoutOthers.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBANoutOthers.setDescription('Count of other packets not counted by the other outgoing counters.')
mibBuilder.exportSymbols("BOUNDARY-ACCESSS-NODE-MIB", ibmBANoutXIDRsps=ibmBANoutXIDRsps, ibmBANinIFrames=ibmBANinIFrames, ibmBANstatus=ibmBANstatus, ibmBANinOthers=ibmBANinOthers, ibmBANoutTestRsps=ibmBANoutTestRsps, ibmBANoutOthers=ibmBANoutOthers, ibmBANoutFRMRs=ibmBANoutFRMRs, ibmBANoutTests=ibmBANoutTests, ibmBANinTests=ibmBANinTests, ibmBANifIndex=ibmBANifIndex, ibmBANinTestRsps=ibmBANinTestRsps, ibmBANoutRNRs=ibmBANoutRNRs, ibmBANinXIDRsps=ibmBANinXIDRsps, ibmBANbridgePort=ibmBANbridgePort, ibmBANtype=ibmBANtype, ibmBANinDISCs=ibmBANinDISCs, ibmBANoutIFrames=ibmBANoutIFrames, ibmBANinRRs=ibmBANinRRs, ibmBANEntry=ibmBANEntry, ibmBANoutDMs=ibmBANoutDMs, ibmBANinDMs=ibmBANinDMs, ibmBANinUAs=ibmBANinUAs, ibmBANMIB=ibmBANMIB, ibmBANoutXIDs=ibmBANoutXIDs, ibmBANinFRMRs=ibmBANinFRMRs, ibmBANinRNRs=ibmBANinRNRs, ibmBANoutRRs=ibmBANoutRRs, ibmBANoutRejs=ibmBANoutRejs, ibmBANDLCImacAddress=ibmBANDLCImacAddress, ibmBANoutSABMEs=ibmBANoutSABMEs, ibmBANinSABMEs=ibmBANinSABMEs, ibmBANTable=ibmBANTable, ibmBANoutDISCs=ibmBANoutDISCs, ibmBANinRejs=ibmBANinRejs, ibmBANboundaryNodeID=ibmBANboundaryNodeID, ibmBANoutUAs=ibmBANoutUAs, ibmBANinXIDs=ibmBANinXIDs)
