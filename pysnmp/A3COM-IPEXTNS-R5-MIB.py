#
# PySNMP MIB module A3COM-IPEXTNS-R5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/A3COM-IPEXTNS-R5-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:29:20 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibIdentifier, ModuleIdentity, enterprises, Gauge32, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, NotificationType, ObjectIdentity, Bits, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "enterprises", "Gauge32", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "NotificationType", "ObjectIdentity", "Bits", "IpAddress", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
brouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2))
a3ComIPextns = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 6))
class SMDSAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

a3IPextMode = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("multipleNet", 1), ("singleNet", 2))).clone('multipleNet')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPextMode.setStatus('mandatory')
a3IPextFlushCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("flushRoutes", 2), ("flushARP", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPextFlushCtl.setStatus('mandatory')
a3IPextRelaySrcRteCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("relay", 1), ("discard", 2))).clone('discard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPextRelaySrcRteCtl.setStatus('mandatory')
a3IPextSplitLoadCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("split", 1), ("noSplit", 2))).clone('noSplit')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPextSplitLoadCtl.setStatus('mandatory')
a3IPicmpInfoCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("info", 1), ("noInfo", 2))).clone('noInfo')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPicmpInfoCtl.setStatus('mandatory')
a3IPicmpMaskCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mask", 1), ("noMask", 2))).clone('noMask')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPicmpMaskCtl.setStatus('mandatory')
a3IPntmExtTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 7), )
if mibBuilder.loadTexts: a3IPntmExtTable.setStatus('mandatory')
a3IPntmExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IPntmIfIndex"), (0, "A3COM-IPEXTNS-R5-MIB", "a3IPntmNetAddress"))
if mibBuilder.loadTexts: a3IPntmExtEntry.setStatus('mandatory')
a3IPntmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPntmIfIndex.setStatus('mandatory')
a3IPntmNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPntmNetAddress.setStatus('mandatory')
a3IPntmHdrFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ethernet", 2), ("ieee", 3), ("snap", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPntmHdrFormat.setStatus('mandatory')
a3IPntmProxyArp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("proxy", 1), ("noProxy", 2))).clone('noProxy')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPntmProxyArp.setStatus('mandatory')
a3IPaddrConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 8), )
if mibBuilder.loadTexts: a3IPaddrConfigTable.setStatus('mandatory')
a3IPaddrConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IPaddrConfigPort"), (0, "A3COM-IPEXTNS-R5-MIB", "a3IPaddrConfigAddr"))
if mibBuilder.loadTexts: a3IPaddrConfigEntry.setStatus('mandatory')
a3IPaddrConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPaddrConfigPort.setStatus('mandatory')
a3IPaddrConfigAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPaddrConfigAddr.setStatus('mandatory')
a3IPaddrConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2))).clone('primary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPaddrConfigType.setStatus('mandatory')
a3IPaddrConfigNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPaddrConfigNetMask.setStatus('mandatory')
a3IPaddrConfigBcastAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 5), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPaddrConfigBcastAddr.setStatus('mandatory')
a3IPaddrConfigMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(68, 32767))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPaddrConfigMtu.setStatus('mandatory')
a3IPaddrConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 8, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPaddrConfigStatus.setStatus('mandatory')
a3IPforwardExtTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 9), )
if mibBuilder.loadTexts: a3IPforwardExtTable.setStatus('mandatory')
a3IPforwardExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IPforwardExtDest"), (0, "A3COM-IPEXTNS-R5-MIB", "a3IPforwardExtProto"), (0, "A3COM-IPEXTNS-R5-MIB", "a3IPforwardExtPolicy"), (0, "A3COM-IPEXTNS-R5-MIB", "a3IPforwardExtNextHop"))
if mibBuilder.loadTexts: a3IPforwardExtEntry.setStatus('mandatory')
a3IPforwardExtDest = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPforwardExtDest.setStatus('mandatory')
a3IPforwardExtProto = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("is-is", 9), ("es-is", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPforwardExtProto.setStatus('mandatory')
a3IPforwardExtPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPforwardExtPolicy.setStatus('mandatory')
a3IPforwardExtNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPforwardExtNextHop.setStatus('mandatory')
a3IPforwardExtOverride = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("override", 1), ("noOverride", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPforwardExtOverride.setStatus('mandatory')
a3IParpOverBlocked = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IParpOverBlocked.setStatus('mandatory')
a3IPrarpClientCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPrarpClientCtl.setStatus('mandatory')
a3IPrarpServerCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPrarpServerCtl.setStatus('mandatory')
a3IParpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 13), )
if mibBuilder.loadTexts: a3IParpConfigTable.setStatus('mandatory')
a3IParpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IParpPortIndex"))
if mibBuilder.loadTexts: a3IParpConfigEntry.setStatus('mandatory')
a3IParpPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IParpPortIndex.setStatus('mandatory')
a3IParpProxyCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("proxy", 1), ("noProxy", 2))).clone('noProxy')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IParpProxyCtl.setStatus('mandatory')
a3IParpHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24)).clone(24)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IParpHoldTime.setStatus('mandatory')
a3IParpReqFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 128, 129, 130, 131))).clone(namedValues=NamedValues(("ethernet", 1), ("snap", 2), ("both", 3), ("auto", 128), ("ethAuto", 129), ("snapAuto", 130), ("bothAuto", 131))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IParpReqFormat.setStatus('mandatory')
a3IParpRemAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IParpRemAddr.setStatus('mandatory')
a3IParpInvCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 13, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IParpInvCtl.setStatus('mandatory')
a3IPsmdsGaTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 14), )
if mibBuilder.loadTexts: a3IPsmdsGaTable.setStatus('mandatory')
a3IPsmdsGaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 14, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IPsmdsGaIpNet"))
if mibBuilder.loadTexts: a3IPsmdsGaEntry.setStatus('mandatory')
a3IPsmdsGaIpNet = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 14, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPsmdsGaIpNet.setStatus('mandatory')
a3IPsmdsGa = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 14, 1, 2), SMDSAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsmdsGa.setStatus('mandatory')
a3IPsmdsGaStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 14, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPsmdsGaStatus.setStatus('mandatory')
a3IPx25configTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 15), )
if mibBuilder.loadTexts: a3IPx25configTable.setStatus('mandatory')
a3IPx25configEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IPx25configPort"))
if mibBuilder.loadTexts: a3IPx25configEntry.setStatus('mandatory')
a3IPx25configPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPx25configPort.setStatus('mandatory')
a3IPx25configPID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(204)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPx25configPID.setStatus('mandatory')
a3IPx25configQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPx25configQueueSize.setStatus('deprecated')
a3IPx25configVClimit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPx25configVClimit.setStatus('deprecated')
a3IPx25configVCtimer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPx25configVCtimer.setStatus('deprecated')
a3IPx25configProfID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 15, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPx25configProfID.setStatus('mandatory')
a3IPqueuePriority = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("high", 1), ("medium", 2), ("low", 3), ("default", 4), ("unknown", 5))).clone('medium')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPqueuePriority.setStatus('mandatory')
a3IPfwdSubnetBcast = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 6, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fwdSubnetBcast", 1), ("noFwdSubnetBcast", 2))).clone('noFwdSubnetBcast')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPfwdSubnetBcast.setStatus('mandatory')
a3IPicmpGenTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 6, 18), )
if mibBuilder.loadTexts: a3IPicmpGenTable.setStatus('mandatory')
a3IPicmpGenEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1), ).setIndexNames((0, "A3COM-IPEXTNS-R5-MIB", "a3IPicmpGenIfIndex"))
if mibBuilder.loadTexts: a3IPicmpGenEntry.setStatus('mandatory')
a3IPicmpGenIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3IPicmpGenIfIndex.setStatus('mandatory')
a3IPicmpGenRedirect = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("redirect", 1), ("noRedirect", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPicmpGenRedirect.setStatus('mandatory')
a3IPicmpGenDestUnreach = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("destUnreachable", 1), ("noDestUnreachable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPicmpGenDestUnreach.setStatus('mandatory')
a3IPicmpGenTimeExceed = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 6, 18, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("timeExceed", 1), ("noTimeExceed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3IPicmpGenTimeExceed.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-IPEXTNS-R5-MIB", a3IParpProxyCtl=a3IParpProxyCtl, a3IPntmExtEntry=a3IPntmExtEntry, a3IPextFlushCtl=a3IPextFlushCtl, a3IPextMode=a3IPextMode, a3IPaddrConfigPort=a3IPaddrConfigPort, a3IPx25configProfID=a3IPx25configProfID, a3IParpConfigTable=a3IParpConfigTable, a3IPfwdSubnetBcast=a3IPfwdSubnetBcast, a3IPicmpMaskCtl=a3IPicmpMaskCtl, a3IPx25configVCtimer=a3IPx25configVCtimer, a3IPntmProxyArp=a3IPntmProxyArp, a3IPrarpServerCtl=a3IPrarpServerCtl, a3IParpPortIndex=a3IParpPortIndex, a3IPicmpGenDestUnreach=a3IPicmpGenDestUnreach, a3IPx25configTable=a3IPx25configTable, SMDSAddress=SMDSAddress, a3IPforwardExtNextHop=a3IPforwardExtNextHop, a3IPx25configPID=a3IPx25configPID, brouterMIB=brouterMIB, a3Com=a3Com, a3IPforwardExtProto=a3IPforwardExtProto, a3IPsmdsGaEntry=a3IPsmdsGaEntry, a3IParpOverBlocked=a3IParpOverBlocked, a3IPntmIfIndex=a3IPntmIfIndex, a3IPsmdsGaTable=a3IPsmdsGaTable, a3IPsmdsGa=a3IPsmdsGa, a3IPicmpGenEntry=a3IPicmpGenEntry, a3IPicmpGenRedirect=a3IPicmpGenRedirect, a3IPntmNetAddress=a3IPntmNetAddress, a3IPforwardExtEntry=a3IPforwardExtEntry, a3IPrarpClientCtl=a3IPrarpClientCtl, a3IPaddrConfigMtu=a3IPaddrConfigMtu, a3IParpHoldTime=a3IParpHoldTime, a3IParpRemAddr=a3IParpRemAddr, a3IPforwardExtDest=a3IPforwardExtDest, a3IPaddrConfigTable=a3IPaddrConfigTable, a3IPx25configEntry=a3IPx25configEntry, a3ComIPextns=a3ComIPextns, a3IPaddrConfigAddr=a3IPaddrConfigAddr, a3IParpReqFormat=a3IParpReqFormat, a3IPicmpGenTimeExceed=a3IPicmpGenTimeExceed, a3IPicmpGenTable=a3IPicmpGenTable, a3IPaddrConfigType=a3IPaddrConfigType, a3IPntmExtTable=a3IPntmExtTable, a3IPextRelaySrcRteCtl=a3IPextRelaySrcRteCtl, a3IPextSplitLoadCtl=a3IPextSplitLoadCtl, a3IPicmpInfoCtl=a3IPicmpInfoCtl, a3IPaddrConfigEntry=a3IPaddrConfigEntry, a3IParpInvCtl=a3IParpInvCtl, a3IPqueuePriority=a3IPqueuePriority, a3IPforwardExtOverride=a3IPforwardExtOverride, a3IPaddrConfigBcastAddr=a3IPaddrConfigBcastAddr, a3IPx25configPort=a3IPx25configPort, a3IPsmdsGaStatus=a3IPsmdsGaStatus, a3IPicmpGenIfIndex=a3IPicmpGenIfIndex, a3IPaddrConfigStatus=a3IPaddrConfigStatus, a3IPntmHdrFormat=a3IPntmHdrFormat, a3IParpConfigEntry=a3IParpConfigEntry, a3IPforwardExtTable=a3IPforwardExtTable, a3IPsmdsGaIpNet=a3IPsmdsGaIpNet, a3IPaddrConfigNetMask=a3IPaddrConfigNetMask, a3IPforwardExtPolicy=a3IPforwardExtPolicy, RowStatus=RowStatus, a3IPx25configQueueSize=a3IPx25configQueueSize, a3IPx25configVClimit=a3IPx25configVClimit)
