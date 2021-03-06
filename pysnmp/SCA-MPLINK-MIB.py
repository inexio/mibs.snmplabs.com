#
# PySNMP MIB module SCA-MPLINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCA-MPLINK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
scanet, = mibBuilder.importSymbols("SCANET-MIB", "scanet")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Bits, MibIdentifier, NotificationType, iso, Counter32, Unsigned32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Bits", "MibIdentifier", "NotificationType", "iso", "Counter32", "Unsigned32", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class OffOn(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("off", 1), ("on", 2))

mplk = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 24))
service = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 24, 1))
lanSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 24, 2))
wanSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 24, 3))
serviceTable = MibTable((1, 3, 6, 1, 4, 1, 208, 24, 1, 1), )
if mibBuilder.loadTexts: serviceTable.setStatus('mandatory')
serviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1), ).setIndexNames((0, "SCA-MPLINK-MIB", "serviceNumber1"))
if mibBuilder.loadTexts: serviceEntry.setStatus('mandatory')
serviceNumber1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceNumber1.setStatus('mandatory')
serviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceName.setStatus('mandatory')
serviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("static", 1), ("aod", 2), ("pod", 3), ("pool", 4), ("internal", 5), ("lan", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceType.setStatus('mandatory')
slot = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slot.setStatus('mandatory')
plug = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: plug.setStatus('mandatory')
serviceState = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("outOfService", 1), ("noProvider", 2), ("down", 3), ("timeCut", 4), ("up", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceState.setStatus('mandatory')
bytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bytesSent.setStatus('mandatory')
bytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bytesReceived.setStatus('mandatory')
packetsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: packetsSent.setStatus('mandatory')
packetsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: packetsReceived.setStatus('mandatory')
maxPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxPacketSize.setStatus('mandatory')
lanTable = MibTable((1, 3, 6, 1, 4, 1, 208, 24, 2, 1), )
if mibBuilder.loadTexts: lanTable.setStatus('mandatory')
lanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 24, 2, 1, 1), ).setIndexNames((0, "SCA-MPLINK-MIB", "serviceNumber2"))
if mibBuilder.loadTexts: lanEntry.setStatus('mandatory')
serviceNumber2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceNumber2.setStatus('mandatory')
ownSNPAAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ownSNPAAddress.setStatus('mandatory')
scaNetSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scaNetSubnet.setStatus('mandatory')
incomingAccessMask1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: incomingAccessMask1.setStatus('mandatory')
outgoingAccessMask1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outgoingAccessMask1.setStatus('mandatory')
wanTable = MibTable((1, 3, 6, 1, 4, 1, 208, 24, 3, 1), )
if mibBuilder.loadTexts: wanTable.setStatus('mandatory')
wanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1), ).setIndexNames((0, "SCA-MPLINK-MIB", "serviceNumber3"))
if mibBuilder.loadTexts: wanEntry.setStatus('mandatory')
serviceNumber3 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceNumber3.setStatus('mandatory')
provider = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: provider.setStatus('mandatory')
queueActualValue = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueActualValue.setStatus('mandatory')
queueHighWaterTideMark = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueHighWaterTideMark.setStatus('mandatory')
queueRejectThreshold1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: queueRejectThreshold1.setStatus('mandatory')
dataCompressionSwitch1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 6), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataCompressionSwitch1.setStatus('mandatory')
dataCompressionState = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 7), OffOn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataCompressionState.setStatus('mandatory')
acceptIncomingCalls1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 8), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acceptIncomingCalls1.setStatus('mandatory')
permitOutgoingCalls1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 9), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: permitOutgoingCalls1.setStatus('mandatory')
acceptReverseCharge1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 10), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acceptReverseCharge1.setStatus('mandatory')
proposeReverseCharge1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 11), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: proposeReverseCharge1.setStatus('mandatory')
permitTimeCut1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 12), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: permitTimeCut1.setStatus('mandatory')
backupOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 13), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupOnly.setStatus('mandatory')
actualCallState = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("outOfService", 1), ("noProvider", 2), ("error", 3), ("down", 4), ("disconnecting", 5), ("connecting", 6), ("up", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: actualCallState.setStatus('mandatory')
actualCallDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inc", 1), ("outg", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: actualCallDirection.setStatus('mandatory')
actualCallDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: actualCallDuration.setStatus('mandatory')
minCallDuration1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: minCallDuration1.setStatus('mandatory')
idleTime1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idleTime1.setStatus('mandatory')
actualTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: actualTimer.setStatus('mandatory')
reserveTime1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reserveTime1.setStatus('mandatory')
ownUserDataAddress1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ownUserDataAddress1.setStatus('mandatory')
remoteSNPAaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 22), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: remoteSNPAaddress.setStatus('mandatory')
remoteUserDataAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: remoteUserDataAddress.setStatus('mandatory')
callsPlaced1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callsPlaced1.setStatus('mandatory')
callsFailed1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callsFailed1.setStatus('mandatory')
actualErrorRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: actualErrorRetries.setStatus('mandatory')
maxErrorRetries1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 27), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maxErrorRetries1.setStatus('mandatory')
errorRetryInterval1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 28), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: errorRetryInterval1.setStatus('mandatory')
maxCallSetupTime1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 29), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maxCallSetupTime1.setStatus('mandatory')
mostRecentFailure1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 30), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mostRecentFailure1.setStatus('mandatory')
backupForLink = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 31), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupForLink.setStatus('mandatory')
poolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 32), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poolIndex.setStatus('mandatory')
incomingAccessMask2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 33), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: incomingAccessMask2.setStatus('mandatory')
outgoingAccessMask2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 34), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outgoingAccessMask2.setStatus('mandatory')
timecutAccessMask1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 35), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timecutAccessMask1.setStatus('mandatory')
poolTable = MibTable((1, 3, 6, 1, 4, 1, 208, 24, 3, 2), )
if mibBuilder.loadTexts: poolTable.setStatus('mandatory')
poolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1), ).setIndexNames((0, "SCA-MPLINK-MIB", "serviceNumber4"))
if mibBuilder.loadTexts: poolEntry.setStatus('mandatory')
serviceNumber4 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceNumber4.setStatus('mandatory')
poolName = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolName.setStatus('mandatory')
queueRejectThreshold2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: queueRejectThreshold2.setStatus('mandatory')
dataCompressionSwitch2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 4), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataCompressionSwitch2.setStatus('mandatory')
acceptIncomingCalls2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 5), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acceptIncomingCalls2.setStatus('mandatory')
permitOutgoingCalls2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 6), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: permitOutgoingCalls2.setStatus('mandatory')
acceptReverseCharge2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 7), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acceptReverseCharge2.setStatus('mandatory')
proposeReverseCharge2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 8), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: proposeReverseCharge2.setStatus('mandatory')
permitTimeCut2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 9), OffOn()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: permitTimeCut2.setStatus('mandatory')
minCallDuration2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: minCallDuration2.setStatus('mandatory')
idleTime2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idleTime2.setStatus('mandatory')
reserveTime2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: reserveTime2.setStatus('mandatory')
ownUserDataAddress2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ownUserDataAddress2.setStatus('mandatory')
callsPlaced2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callsPlaced2.setStatus('mandatory')
callsFailed2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callsFailed2.setStatus('mandatory')
maxErrorRetries2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maxErrorRetries2.setStatus('mandatory')
errorRetryInterval2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: errorRetryInterval2.setStatus('mandatory')
maxCallSetupTime2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maxCallSetupTime2.setStatus('mandatory')
mostRecentFailure2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 19), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mostRecentFailure2.setStatus('mandatory')
poolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolSize.setStatus('mandatory')
freeLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: freeLinks.setStatus('mandatory')
incomingAccessMask3 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 22), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: incomingAccessMask3.setStatus('mandatory')
outgoingAccessMask3 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 23), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outgoingAccessMask3.setStatus('mandatory')
timecutAccessMask2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timecutAccessMask2.setStatus('mandatory')
mibBuilder.exportSymbols("SCA-MPLINK-MIB", ownUserDataAddress2=ownUserDataAddress2, freeLinks=freeLinks, acceptReverseCharge1=acceptReverseCharge1, lanSpecific=lanSpecific, remoteUserDataAddress=remoteUserDataAddress, mostRecentFailure1=mostRecentFailure1, permitOutgoingCalls1=permitOutgoingCalls1, callsFailed2=callsFailed2, OffOn=OffOn, bytesSent=bytesSent, errorRetryInterval2=errorRetryInterval2, queueRejectThreshold1=queueRejectThreshold1, actualCallDuration=actualCallDuration, dataCompressionSwitch1=dataCompressionSwitch1, maxPacketSize=maxPacketSize, maxCallSetupTime1=maxCallSetupTime1, dataCompressionState=dataCompressionState, reserveTime2=reserveTime2, serviceNumber1=serviceNumber1, service=service, maxCallSetupTime2=maxCallSetupTime2, outgoingAccessMask2=outgoingAccessMask2, incomingAccessMask2=incomingAccessMask2, scaNetSubnet=scaNetSubnet, incomingAccessMask3=incomingAccessMask3, permitOutgoingCalls2=permitOutgoingCalls2, ownUserDataAddress1=ownUserDataAddress1, proposeReverseCharge1=proposeReverseCharge1, backupForLink=backupForLink, bytesReceived=bytesReceived, serviceNumber2=serviceNumber2, serviceState=serviceState, dataCompressionSwitch2=dataCompressionSwitch2, acceptIncomingCalls2=acceptIncomingCalls2, lanEntry=lanEntry, serviceType=serviceType, outgoingAccessMask3=outgoingAccessMask3, maxErrorRetries1=maxErrorRetries1, actualErrorRetries=actualErrorRetries, wanEntry=wanEntry, actualCallState=actualCallState, serviceName=serviceName, acceptReverseCharge2=acceptReverseCharge2, proposeReverseCharge2=proposeReverseCharge2, maxErrorRetries2=maxErrorRetries2, remoteSNPAaddress=remoteSNPAaddress, poolName=poolName, wanSpecific=wanSpecific, actualCallDirection=actualCallDirection, acceptIncomingCalls1=acceptIncomingCalls1, outgoingAccessMask1=outgoingAccessMask1, plug=plug, incomingAccessMask1=incomingAccessMask1, timecutAccessMask1=timecutAccessMask1, callsFailed1=callsFailed1, serviceEntry=serviceEntry, provider=provider, ownSNPAAddress=ownSNPAAddress, packetsReceived=packetsReceived, slot=slot, permitTimeCut1=permitTimeCut1, mostRecentFailure2=mostRecentFailure2, reserveTime1=reserveTime1, backupOnly=backupOnly, callsPlaced1=callsPlaced1, callsPlaced2=callsPlaced2, poolSize=poolSize, actualTimer=actualTimer, permitTimeCut2=permitTimeCut2, mplk=mplk, errorRetryInterval1=errorRetryInterval1, poolEntry=poolEntry, lanTable=lanTable, poolTable=poolTable, serviceTable=serviceTable, queueHighWaterTideMark=queueHighWaterTideMark, minCallDuration1=minCallDuration1, timecutAccessMask2=timecutAccessMask2, idleTime1=idleTime1, serviceNumber3=serviceNumber3, queueRejectThreshold2=queueRejectThreshold2, packetsSent=packetsSent, minCallDuration2=minCallDuration2, poolIndex=poolIndex, idleTime2=idleTime2, serviceNumber4=serviceNumber4, queueActualValue=queueActualValue, wanTable=wanTable)
