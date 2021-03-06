#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:19:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, TimeTicks, MibIdentifier, enterprises, Counter32, Unsigned32, Gauge32, Counter64, Integer32, iso, ModuleIdentity, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "TimeTicks", "MibIdentifier", "enterprises", "Counter32", "Unsigned32", "Gauge32", "Counter64", "Integer32", "iso", "ModuleIdentity", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nortel = MibIdentifier((1, 3, 6, 1, 4, 1, 562))
msCarrier = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36))
mscProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 1))
mscPassport = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2))
mscPassport7440 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 1, 1))
mscPassport7480 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 1, 2))
mscPassportVirtualRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 1, 3))
mscPassport15000 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 1, 4))
mscComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1))
mscPassportMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2))
usefulDefinitionsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1))
mscPassportTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3))
usefulDefinitionsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 1))
usefulDefinitionsGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 1, 1))
usefulDefinitionsGroupCA01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 1, 1, 2))
usefulDefinitionsGroupCA01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 1, 1, 2, 2))
usefulDefinitionsCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 3))
usefulDefinitionsCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 3, 1))
usefulDefinitionsCapabilitiesCA01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 3, 1, 2))
usefulDefinitionsCapabilitiesCA01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 3, 1, 2, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", mscPassportVirtualRouter=mscPassportVirtualRouter, mscPassport7480=mscPassport7480, mscPassport15000=mscPassport15000, usefulDefinitionsGroupCA01A=usefulDefinitionsGroupCA01A, usefulDefinitionsMIB=usefulDefinitionsMIB, nortel=nortel, mscPassportMIBs=mscPassportMIBs, usefulDefinitionsGroupCA01=usefulDefinitionsGroupCA01, mscProducts=mscProducts, mscComponents=mscComponents, usefulDefinitionsGroupCA=usefulDefinitionsGroupCA, mscPassport7440=mscPassport7440, mscPassportTraps=mscPassportTraps, msCarrier=msCarrier, usefulDefinitionsCapabilitiesCA01A=usefulDefinitionsCapabilitiesCA01A, mscPassport=mscPassport, usefulDefinitionsCapabilitiesCA01=usefulDefinitionsCapabilitiesCA01, usefulDefinitionsCapabilities=usefulDefinitionsCapabilities, usefulDefinitionsCapabilitiesCA=usefulDefinitionsCapabilitiesCA, usefulDefinitionsGroup=usefulDefinitionsGroup)
