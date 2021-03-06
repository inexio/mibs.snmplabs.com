#
# PySNMP MIB module FASTPATH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:12:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, enterprises, iso, Counter32, Integer32, Unsigned32, ObjectIdentity, TimeTicks, Bits, Gauge32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "enterprises", "iso", "Counter32", "Integer32", "Unsigned32", "ObjectIdentity", "TimeTicks", "Bits", "Gauge32", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
excelan = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
genericGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2))
fastpathMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11))
scc = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11, 1))
alap = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11, 2))
ethernet = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11, 3))
aarp = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11, 4))
atif = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11, 5))
ddp = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11, 6))
rtmp = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11, 7))
kip = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11, 8))
zip = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11, 9))
nbp = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11, 10))
echo = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11, 11))
buffer = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 11, 12))
sccInterruptCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccInterruptCount.setStatus('mandatory')
sccAbortCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccAbortCount.setStatus('mandatory')
sccSpuriousCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccSpuriousCount.setStatus('mandatory')
sccCRCCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccCRCCount.setStatus('mandatory')
sccOverrunCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccOverrunCount.setStatus('mandatory')
sccUnderrunCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccUnderrunCount.setStatus('mandatory')
alapReceiveCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alapReceiveCount.setStatus('mandatory')
alapTransmitCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alapTransmitCount.setStatus('mandatory')
alapNoHandlerCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alapNoHandlerCount.setStatus('mandatory')
alapLengthErrorCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alapLengthErrorCount.setStatus('mandatory')
alapBadCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alapBadCount.setStatus('mandatory')
alapCollisionCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alapCollisionCount.setStatus('mandatory')
alapDeferCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alapDeferCount.setStatus('mandatory')
alapNoDataCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alapNoDataCount.setStatus('mandatory')
alapRandomCTS = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alapRandomCTS.setStatus('mandatory')
etherCRCErrors = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherCRCErrors.setStatus('mandatory')
etherAlignErrors = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherAlignErrors.setStatus('mandatory')
etherResourceErrors = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherResourceErrors.setStatus('mandatory')
etherOverrunErrors = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherOverrunErrors.setStatus('mandatory')
etherInPackets = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherInPackets.setStatus('mandatory')
etherOutPackets = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherOutPackets.setStatus('mandatory')
etherBadTransmits = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherBadTransmits.setStatus('mandatory')
etherOversizeFrames = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherOversizeFrames.setStatus('mandatory')
etherSpurRUReadys = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherSpurRUReadys.setStatus('mandatory')
etherSpurCUActives = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherSpurCUActives.setStatus('mandatory')
etherSpurUnknown = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherSpurUnknown.setStatus('mandatory')
etherBcastDrops = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherBcastDrops.setStatus('mandatory')
etherReceiverRestarts = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherReceiverRestarts.setStatus('mandatory')
etherReinterrupts = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherReinterrupts.setStatus('mandatory')
etherBufferReroutes = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherBufferReroutes.setStatus('mandatory')
etherBufferDrops = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherBufferDrops.setStatus('mandatory')
etherCollisions = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherCollisions.setStatus('mandatory')
etherDefers = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherDefers.setStatus('mandatory')
etherDMAUnderruns = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherDMAUnderruns.setStatus('mandatory')
etherMaxCollisions = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherMaxCollisions.setStatus('mandatory')
etherNoCarriers = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherNoCarriers.setStatus('mandatory')
etherNoCTS = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherNoCTS.setStatus('mandatory')
etherNoSQEs = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherNoSQEs.setStatus('mandatory')
aarpTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 11, 4, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aarpTable.setStatus('mandatory')
aarpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 11, 4, 1, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aarpEntry.setStatus('mandatory')
aarpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aarpIfIndex.setStatus('mandatory')
aarpPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 4, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aarpPhysAddress.setStatus('mandatory')
aarpNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 4, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aarpNetAddress.setStatus('mandatory')
atifTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atifTable.setStatus('mandatory')
atifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atifEntry.setStatus('mandatory')
atifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atifIndex.setStatus('mandatory')
atifDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atifDescr.setStatus('mandatory')
atifType = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("localtalk", 2), ("ethertalk1", 3), ("ethertalk2", 4), ("tokentalk", 5), ("iptalk", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atifType.setStatus('mandatory')
atifNetStart = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atifNetStart.setStatus('mandatory')
atifNetEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atifNetEnd.setStatus('mandatory')
atifNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atifNetAddress.setStatus('mandatory')
atifStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atifStatus.setStatus('mandatory')
atifNetConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("configured", 1), ("garnered", 2), ("guessed", 3), ("unconfigured", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atifNetConfig.setStatus('mandatory')
atifZoneConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("configured", 1), ("garnered", 2), ("guessed", 3), ("unconfigured", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atifZoneConfig.setStatus('mandatory')
atifZone = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 10), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atifZone.setStatus('mandatory')
atifIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atifIfIndex.setStatus('mandatory')
ddpOutRequests = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpOutRequests.setStatus('mandatory')
ddpOutShort = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpOutShort.setStatus('mandatory')
ddpOutLong = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpOutLong.setStatus('mandatory')
ddpReceived = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpReceived.setStatus('mandatory')
ddpToForward = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpToForward.setStatus('mandatory')
ddpForwards = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpForwards.setStatus('mandatory')
ddpForMe = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpForMe.setStatus('mandatory')
ddpOutNoRoutes = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpOutNoRoutes.setStatus('mandatory')
ddpTooShortDrops = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpTooShortDrops.setStatus('mandatory')
ddpTooLongDrops = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpTooLongDrops.setStatus('mandatory')
ddpBroadcastDrops = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpBroadcastDrops.setStatus('mandatory')
ddpShortDDPDrops = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpShortDDPDrops.setStatus('mandatory')
ddpHopCountDrops = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddpHopCountDrops.setStatus('mandatory')
rtmpTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtmpTable.setStatus('mandatory')
rtmpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtmpEntry.setStatus('mandatory')
rtmpRangeStart = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtmpRangeStart.setStatus('mandatory')
rtmpRangeEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtmpRangeEnd.setStatus('mandatory')
rtmpNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtmpNextHop.setStatus('mandatory')
rtmpInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtmpInterface.setStatus('mandatory')
rtmpHops = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtmpHops.setStatus('mandatory')
rtmpState = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("good", 1), ("suspect", 2), ("bad", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtmpState.setStatus('mandatory')
kipTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: kipTable.setStatus('mandatory')
kipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: kipEntry.setStatus('mandatory')
kipNet = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: kipNet.setStatus('mandatory')
kipNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: kipNextHop.setStatus('mandatory')
kipHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: kipHopCount.setStatus('mandatory')
kipBCastAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: kipBCastAddr.setStatus('mandatory')
kipCore = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("core", 1), ("notcore", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: kipCore.setStatus('mandatory')
kipKfps = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: kipKfps.setStatus('mandatory')
zipTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 11, 9, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zipTable.setStatus('mandatory')
zipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 11, 9, 1, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zipEntry.setStatus('mandatory')
zipZoneName = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 9, 1, 1, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zipZoneName.setStatus('mandatory')
zipZoneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 9, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zipZoneIndex.setStatus('mandatory')
zipZoneNetStart = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 9, 1, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zipZoneNetStart.setStatus('mandatory')
zipZoneNetEnd = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 9, 1, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zipZoneNetEnd.setStatus('mandatory')
nbpTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 11, 10, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbpTable.setStatus('mandatory')
nbpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 11, 10, 1, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbpEntry.setStatus('mandatory')
nbpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbpIndex.setStatus('mandatory')
nbpObject = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 10, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbpObject.setStatus('mandatory')
nbpType = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 10, 1, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbpType.setStatus('mandatory')
nbpZone = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 10, 1, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbpZone.setStatus('mandatory')
echoRequests = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 11, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: echoRequests.setStatus('mandatory')
echoReplies = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 11, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: echoReplies.setStatus('mandatory')
bufferSize = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferSize.setStatus('mandatory')
bufferAvail = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferAvail.setStatus('mandatory')
bufferDrops = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferDrops.setStatus('mandatory')
bufferTypeTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 4), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeTable.setStatus('mandatory')
bufferTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 4, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeEntry.setStatus('mandatory')
bufferTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeIndex.setStatus('mandatory')
bufferType = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("other", 1), ("free", 2), ("localtalk", 3), ("ethernet", 4), ("arp", 5), ("data", 6), ("erbf", 7), ("etbf", 8), ("malloc", 9), ("tkbf", 10), ("token", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferType.setStatus('mandatory')
bufferTypeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 4, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeDescr.setStatus('mandatory')
bufferTypeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeCount.setStatus('mandatory')
mibBuilder.exportSymbols("FASTPATH-MIB", etherAlignErrors=etherAlignErrors, ddpOutNoRoutes=ddpOutNoRoutes, alapCollisionCount=alapCollisionCount, bufferAvail=bufferAvail, kipKfps=kipKfps, etherReceiverRestarts=etherReceiverRestarts, bufferTypeTable=bufferTypeTable, kipCore=kipCore, atifIndex=atifIndex, alapDeferCount=alapDeferCount, rtmpRangeStart=rtmpRangeStart, etherResourceErrors=etherResourceErrors, etherOversizeFrames=etherOversizeFrames, bufferTypeEntry=bufferTypeEntry, ddpOutRequests=ddpOutRequests, ddp=ddp, zipTable=zipTable, etherBadTransmits=etherBadTransmits, nbpTable=nbpTable, alap=alap, bufferDrops=bufferDrops, bufferType=bufferType, sccCRCCount=sccCRCCount, alapReceiveCount=alapReceiveCount, rtmpState=rtmpState, atifEntry=atifEntry, sccAbortCount=sccAbortCount, ddpToForward=ddpToForward, echo=echo, etherOverrunErrors=etherOverrunErrors, atifZoneConfig=atifZoneConfig, atifTable=atifTable, ddpForwards=ddpForwards, bufferTypeIndex=bufferTypeIndex, rtmpNextHop=rtmpNextHop, aarpNetAddress=aarpNetAddress, atif=atif, alapTransmitCount=alapTransmitCount, alapNoHandlerCount=alapNoHandlerCount, etherDMAUnderruns=etherDMAUnderruns, alapBadCount=alapBadCount, etherReinterrupts=etherReinterrupts, ddpTooShortDrops=ddpTooShortDrops, aarpPhysAddress=aarpPhysAddress, aarpIfIndex=aarpIfIndex, rtmpTable=rtmpTable, zipZoneIndex=zipZoneIndex, etherMaxCollisions=etherMaxCollisions, atifStatus=atifStatus, aarpEntry=aarpEntry, etherSpurUnknown=etherSpurUnknown, zipZoneNetStart=zipZoneNetStart, kipEntry=kipEntry, sccOverrunCount=sccOverrunCount, aarpTable=aarpTable, nbpObject=nbpObject, atifZone=atifZone, kipTable=kipTable, ddpForMe=ddpForMe, etherBufferDrops=etherBufferDrops, atifDescr=atifDescr, etherOutPackets=etherOutPackets, zipEntry=zipEntry, bufferSize=bufferSize, nbpEntry=nbpEntry, echoRequests=echoRequests, etherDefers=etherDefers, atifType=atifType, rtmpHops=rtmpHops, atifNetStart=atifNetStart, kipBCastAddr=kipBCastAddr, ethernet=ethernet, fastpathMib=fastpathMib, aarp=aarp, sccUnderrunCount=sccUnderrunCount, ddpBroadcastDrops=ddpBroadcastDrops, rtmpEntry=rtmpEntry, etherInPackets=etherInPackets, etherBcastDrops=etherBcastDrops, etherNoCTS=etherNoCTS, kipNextHop=kipNextHop, ddpOutShort=ddpOutShort, echoReplies=echoReplies, nbp=nbp, etherCollisions=etherCollisions, nbpIndex=nbpIndex, rtmp=rtmp, scc=scc, atifNetEnd=atifNetEnd, alapLengthErrorCount=alapLengthErrorCount, etherBufferReroutes=etherBufferReroutes, zipZoneNetEnd=zipZoneNetEnd, bufferTypeCount=bufferTypeCount, alapRandomCTS=alapRandomCTS, sccInterruptCount=sccInterruptCount, zipZoneName=zipZoneName, etherSpurRUReadys=etherSpurRUReadys, nbpZone=nbpZone, ddpReceived=ddpReceived, ddpShortDDPDrops=ddpShortDDPDrops, buffer=buffer, rtmpRangeEnd=rtmpRangeEnd, alapNoDataCount=alapNoDataCount, zip=zip, nbpType=nbpType, sccSpuriousCount=sccSpuriousCount, etherNoCarriers=etherNoCarriers, ddpTooLongDrops=ddpTooLongDrops, ddpHopCountDrops=ddpHopCountDrops, etherNoSQEs=etherNoSQEs, etherCRCErrors=etherCRCErrors, kipNet=kipNet, rtmpInterface=rtmpInterface, kipHopCount=kipHopCount, ddpOutLong=ddpOutLong, atifIfIndex=atifIfIndex, kip=kip, excelan=excelan, atifNetAddress=atifNetAddress, etherSpurCUActives=etherSpurCUActives, bufferTypeDescr=bufferTypeDescr, genericGroup=genericGroup, atifNetConfig=atifNetConfig)
