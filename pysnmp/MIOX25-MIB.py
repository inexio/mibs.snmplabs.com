#
# PySNMP MIB module MIOX25-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///home/tt/fixed_mibs/MIOX25-MIB
# Produced by pysmi-0.0.2 at Mon Jun 22 22:16:41 2015
# On host cray platform Linux version 2.6.37.6-smp by user tt
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( PositiveInteger, ) = mibBuilder.importSymbols("RFC1253-MIB", "PositiveInteger")
( InstancePointer, ) = mibBuilder.importSymbols("RFC1316-MIB", "InstancePointer")
( X121Address, ) = mibBuilder.importSymbols("RFC1382-MIB", "X121Address")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, transmission, TimeTicks, Counter64, NotificationType, iso, Gauge32, MibIdentifier, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "transmission", "TimeTicks", "Counter64", "NotificationType", "iso", "Gauge32", "MibIdentifier", "Bits", "Counter32")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")
miox = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 38))
mioxPle = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 38, 1))
mioxPeer = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 38, 2))
mioxPleTable = MibTable((1, 3, 6, 1, 2, 1, 10, 38, 1, 1), )
mioxPleEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1), ).setIndexNames((0, "MIOX25-MIB", "ifIndex"))
mioxPleMaxCircuits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,2147483647))).setMaxAccess("readwrite")
mioxPleRefusedConnections = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
mioxPleEnAddrToX121LkupFlrs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
mioxPleLastFailedEnAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2,128))).setMaxAccess("readonly")
mioxPleEnAddrToX121LkupFlrTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
mioxPleX121ToEnAddrLkupFlrs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
mioxPleLastFailedX121Address = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 7), X121Address()).setMaxAccess("readonly")
mioxPleX121ToEnAddrLkupFlrTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
mioxPleQbitFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
mioxPleQbitFailureRemoteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 10), X121Address()).setMaxAccess("readonly")
mioxPleQbitFailureTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
mioxPleMinimumOpenTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 12), PositiveInteger()).setMaxAccess("readwrite")
mioxPleInactivityTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 13), PositiveInteger().clone(10000)).setMaxAccess("readwrite")
mioxPleHoldDownTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 14), PositiveInteger()).setMaxAccess("readwrite")
mioxPleCollisionRetryTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 15), PositiveInteger()).setMaxAccess("readwrite")
mioxPleDefaultPeerId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 16), InstancePointer()).setMaxAccess("readwrite")
mioxPeerTable = MibTable((1, 3, 6, 1, 2, 1, 10, 38, 2, 1), )
mioxPeerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1), ).setIndexNames((0, "MIOX25-MIB", "mioxPeerIndex"))
mioxPeerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 1), PositiveInteger()).setMaxAccess("readonly")
mioxPeerStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5, 6,)).clone(namedValues=NamedValues(("valid", 1), ("createRequest", 2), ("underCreation", 3), ("invalid", 4), ("clearCall", 5), ("makeCall", 6),))).setMaxAccess("readwrite")
mioxPeerMaxCircuits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 3), PositiveInteger().clone(1)).setMaxAccess("readwrite")
mioxPeerIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 4), PositiveInteger().clone(1)).setMaxAccess("readwrite")
mioxPeerConnectSeconds = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
mioxPeerX25CallParamId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 6), InstancePointer()).setMaxAccess("readwrite")
mioxPeerEnAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0,128)).clone(hexValue="")).setMaxAccess("readwrite")
mioxPeerX121Address = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 8), X121Address().clone(hexValue="")).setMaxAccess("readwrite")
mioxPeerX25CircuitId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 9), InstancePointer()).setMaxAccess("readwrite")
mioxPeerDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0,255)).clone(hexValue="")).setMaxAccess("readwrite")
mioxPeerEncTable = MibTable((1, 3, 6, 1, 2, 1, 10, 38, 2, 2), )
mioxPeerEncEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 38, 2, 2, 1), ).setIndexNames((0, "MIOX25-MIB", "mioxPeerIndex"), (0, "MIOX25-MIB", "mioxPeerEncIndex"))
mioxPeerEncIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 2, 1, 1), PositiveInteger()).setMaxAccess("readonly")
mioxPeerEncType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 38, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,256))).setMaxAccess("readwrite")
mibBuilder.exportSymbols("MIOX25-MIB", mioxPleX121ToEnAddrLkupFlrs=mioxPleX121ToEnAddrLkupFlrs, mioxPeerX25CallParamId=mioxPeerX25CallParamId, mioxPeerDescr=mioxPeerDescr, mioxPeerIfIndex=mioxPeerIfIndex, mioxPeerEncEntry=mioxPeerEncEntry, mioxPle=mioxPle, mioxPeerMaxCircuits=mioxPeerMaxCircuits, mioxPeerStatus=mioxPeerStatus, mioxPleMaxCircuits=mioxPleMaxCircuits, mioxPeerTable=mioxPeerTable, mioxPleLastFailedX121Address=mioxPleLastFailedX121Address, mioxPleMinimumOpenTimer=mioxPleMinimumOpenTimer, mioxPeerEncType=mioxPeerEncType, mioxPleQbitFailures=mioxPleQbitFailures, mioxPleEnAddrToX121LkupFlrTime=mioxPleEnAddrToX121LkupFlrTime, mioxPeer=mioxPeer, mioxPeerEntry=mioxPeerEntry, mioxPleDefaultPeerId=mioxPleDefaultPeerId, mioxPeerEnAddr=mioxPeerEnAddr, mioxPeerX121Address=mioxPeerX121Address, mioxPleQbitFailureTime=mioxPleQbitFailureTime, mioxPeerConnectSeconds=mioxPeerConnectSeconds, mioxPeerEncTable=mioxPeerEncTable, mioxPleLastFailedEnAddr=mioxPleLastFailedEnAddr, mioxPleEntry=mioxPleEntry, mioxPeerIndex=mioxPeerIndex, mioxPleCollisionRetryTimer=mioxPleCollisionRetryTimer, mioxPleHoldDownTimer=mioxPleHoldDownTimer, mioxPleX121ToEnAddrLkupFlrTime=mioxPleX121ToEnAddrLkupFlrTime, miox=miox, mioxPleTable=mioxPleTable, mioxPleRefusedConnections=mioxPleRefusedConnections, mioxPleQbitFailureRemoteAddress=mioxPleQbitFailureRemoteAddress, mioxPeerEncIndex=mioxPeerEncIndex, mioxPleEnAddrToX121LkupFlrs=mioxPleEnAddrToX121LkupFlrs, mioxPeerX25CircuitId=mioxPeerX25CircuitId, mioxPleInactivityTimer=mioxPleInactivityTimer)