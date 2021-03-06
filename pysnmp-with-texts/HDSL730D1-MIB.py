#
# PySNMP MIB module HDSL730D1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HDSL730D1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
hdsl730D1, = mibBuilder.importSymbols("GDCHDSL-MIB", "hdsl730D1")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ObjectIdentity, Unsigned32, ModuleIdentity, Bits, Integer32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Bits", "Integer32", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hdsl730D1System = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 1))
hdsl730D1Version = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 1, 1))
gdc730D1SystemMIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 11, 4, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdc730D1SystemMIBversion.setStatus('mandatory')
if mibBuilder.loadTexts: gdc730D1SystemMIBversion.setDescription("Identifies the version of the MIB. The format of the version is x.yzT, where 'x' identifies the major revision number, 'y' identifies the minor revision number, 'z' identifies the typographical revision, and T identifies the test revision. Acceptable values for the individual revision components are as follows: x: 1 - 9 y: 0 - 9 z: 0 - 9 T: A - Z Upon formal release, no designation for the test revision will be present.")
hdsl730D1Alarms = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 2))
hdsl730D1NoResponseAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 1))
hdsl730D1DiagRxErrAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 2))
hdsl730D1PowerUpAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 3))
hdsl730D1UnitFailure = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 4))
hdsl730D1ChecksumCorrupt = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 5))
hdsl730D1LossofSignal = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 6))
hdsl730D1UnavailableSec = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 7))
hdsl730D1ErrorSec = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 8))
hdsl730D1LossofSyncWord = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 9))
hdsl730D1MajorBER = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 10))
hdsl730D1MinorBER = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 4, 2, 11))
mibBuilder.exportSymbols("HDSL730D1-MIB", hdsl730D1MinorBER=hdsl730D1MinorBER, hdsl730D1Version=hdsl730D1Version, hdsl730D1Alarms=hdsl730D1Alarms, hdsl730D1PowerUpAlm=hdsl730D1PowerUpAlm, hdsl730D1NoResponseAlm=hdsl730D1NoResponseAlm, hdsl730D1LossofSignal=hdsl730D1LossofSignal, hdsl730D1MajorBER=hdsl730D1MajorBER, hdsl730D1ChecksumCorrupt=hdsl730D1ChecksumCorrupt, gdc730D1SystemMIBversion=gdc730D1SystemMIBversion, hdsl730D1System=hdsl730D1System, hdsl730D1DiagRxErrAlm=hdsl730D1DiagRxErrAlm, hdsl730D1UnitFailure=hdsl730D1UnitFailure, hdsl730D1UnavailableSec=hdsl730D1UnavailableSec, hdsl730D1ErrorSec=hdsl730D1ErrorSec, hdsl730D1LossofSyncWord=hdsl730D1LossofSyncWord)
