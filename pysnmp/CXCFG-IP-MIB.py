#
# PySNMP MIB module CXCFG-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXCFG-IP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:16:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
cxCfgIp, Alias, cxIcmp, cxCfgIpSap = mibBuilder.importSymbols("CXProduct-SMI", "cxCfgIp", "Alias", "cxIcmp", "cxCfgIpSap")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, ObjectIdentity, iso, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, NotificationType, Counter64, Counter32, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "ObjectIdentity", "iso", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "NotificationType", "Counter64", "Counter32", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cxCfgIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1), )
if mibBuilder.loadTexts: cxCfgIpAddrTable.setStatus('mandatory')
cxCfgIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1), ).setIndexNames((0, "CXCFG-IP-MIB", "cxCfgIpAdEntAddr"))
if mibBuilder.loadTexts: cxCfgIpAddrEntry.setStatus('mandatory')
cxCfgIpAdEntAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgIpAdEntAddr.setStatus('mandatory')
cxCfgIpAdEntIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpAdEntIfIndex.setStatus('mandatory')
cxCfgIpAdEntNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpAdEntNetMask.setStatus('mandatory')
cxCfgIpAdEntBcastAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpAdEntBcastAddr.setStatus('mandatory')
cxCfgIpAdEntSubnetworkSAPAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 5), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpAdEntSubnetworkSAPAlias.setStatus('mandatory')
cxCfgIpAdEntRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpAdEntRowStatus.setStatus('mandatory')
cxCfgIpAdEntState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("onether", 3), ("ontoken", 4))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpAdEntState.setStatus('mandatory')
cxCfgIpAdEntPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpAdEntPeerAddr.setStatus('mandatory')
cxCfgIpAdEntRtProto = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("rip", 2), ("ospf", 3))).clone('rip')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpAdEntRtProto.setStatus('mandatory')
cxCfgIpAdEntMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 4096)).clone(1600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpAdEntMtu.setStatus('mandatory')
cxCfgIpAdEntReplyToRARP = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpAdEntReplyToRARP.setStatus('mandatory')
cxCfgIpAdEntSRSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpAdEntSRSupport.setStatus('mandatory')
cxCfgIpPingTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1), )
if mibBuilder.loadTexts: cxCfgIpPingTable.setStatus('mandatory')
cxCfgIpPingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1), ).setIndexNames((0, "CXCFG-IP-MIB", "cxCfgIpPingDestAddr"))
if mibBuilder.loadTexts: cxCfgIpPingEntry.setStatus('mandatory')
cxCfgIpPingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpPingIndex.setStatus('mandatory')
cxCfgIpPingDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpPingDestAddr.setStatus('mandatory')
cxCfgIpPingGapsInMs = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpPingGapsInMs.setStatus('mandatory')
cxCfgIpPingNbOfPings = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4000000)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpPingNbOfPings.setStatus('mandatory')
cxCfgIpPingDataSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpPingDataSize.setStatus('mandatory')
cxCfgIpPingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpPingRowStatus.setStatus('mandatory')
cxCfgIpPingTriggerSend = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipIdle", 1), ("ipSend", 2))).clone('ipIdle')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpPingTriggerSend.setStatus('mandatory')
cxCfgIpPingNbTx = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgIpPingNbTx.setStatus('mandatory')
cxCfgIpPingNbReplyRx = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgIpPingNbReplyRx.setStatus('mandatory')
cxCfgIpPingNbErrorRx = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgIpPingNbErrorRx.setStatus('mandatory')
cxCfgIpPingLastSeqNumRx = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgIpPingLastSeqNumRx.setStatus('mandatory')
cxCfgIpPingLastRoundTripInMs = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgIpPingLastRoundTripInMs.setStatus('mandatory')
cxCfgIpPingAvgRoundTripInMs = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgIpPingAvgRoundTripInMs.setStatus('mandatory')
cxCfgIpPingMinRoundTripInMs = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgIpPingMinRoundTripInMs.setStatus('mandatory')
cxCfgIpPingMaxRoundTripInMs = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgIpPingMaxRoundTripInMs.setStatus('mandatory')
cxCfgIpPingLastNumHopsTraveled = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgIpPingLastNumHopsTraveled.setStatus('mandatory')
cxCfgIpRIP = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgIpRIP.setStatus('mandatory')
cxCfgRIPII = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgRIPII.setStatus('mandatory')
cxCfgIpMibLevel = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgIpMibLevel.setStatus('mandatory')
mibBuilder.exportSymbols("CXCFG-IP-MIB", cxCfgIpPingDestAddr=cxCfgIpPingDestAddr, cxCfgIpPingTriggerSend=cxCfgIpPingTriggerSend, cxCfgIpPingLastSeqNumRx=cxCfgIpPingLastSeqNumRx, cxCfgIpPingAvgRoundTripInMs=cxCfgIpPingAvgRoundTripInMs, cxCfgIpAdEntRtProto=cxCfgIpAdEntRtProto, cxCfgIpAdEntNetMask=cxCfgIpAdEntNetMask, cxCfgIpPingNbTx=cxCfgIpPingNbTx, cxCfgIpAdEntMtu=cxCfgIpAdEntMtu, cxCfgIpPingIndex=cxCfgIpPingIndex, cxCfgIpAdEntReplyToRARP=cxCfgIpAdEntReplyToRARP, cxCfgIpAdEntBcastAddr=cxCfgIpAdEntBcastAddr, cxCfgIpPingNbOfPings=cxCfgIpPingNbOfPings, cxCfgIpPingMinRoundTripInMs=cxCfgIpPingMinRoundTripInMs, cxCfgIpPingLastNumHopsTraveled=cxCfgIpPingLastNumHopsTraveled, cxCfgIpPingMaxRoundTripInMs=cxCfgIpPingMaxRoundTripInMs, cxCfgIpAdEntSRSupport=cxCfgIpAdEntSRSupport, cxCfgIpPingLastRoundTripInMs=cxCfgIpPingLastRoundTripInMs, cxCfgRIPII=cxCfgRIPII, cxCfgIpAdEntSubnetworkSAPAlias=cxCfgIpAdEntSubnetworkSAPAlias, cxCfgIpAdEntRowStatus=cxCfgIpAdEntRowStatus, cxCfgIpMibLevel=cxCfgIpMibLevel, cxCfgIpPingTable=cxCfgIpPingTable, cxCfgIpAddrEntry=cxCfgIpAddrEntry, cxCfgIpPingNbReplyRx=cxCfgIpPingNbReplyRx, cxCfgIpAdEntIfIndex=cxCfgIpAdEntIfIndex, cxCfgIpAdEntState=cxCfgIpAdEntState, cxCfgIpAddrTable=cxCfgIpAddrTable, cxCfgIpPingDataSize=cxCfgIpPingDataSize, cxCfgIpPingRowStatus=cxCfgIpPingRowStatus, cxCfgIpPingGapsInMs=cxCfgIpPingGapsInMs, cxCfgIpRIP=cxCfgIpRIP, cxCfgIpPingNbErrorRx=cxCfgIpPingNbErrorRx, cxCfgIpAdEntPeerAddr=cxCfgIpAdEntPeerAddr, cxCfgIpAdEntAddr=cxCfgIpAdEntAddr, cxCfgIpPingEntry=cxCfgIpPingEntry)
