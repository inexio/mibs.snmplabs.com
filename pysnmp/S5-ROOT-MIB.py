#
# PySNMP MIB module S5-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/S5-ROOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, TimeTicks, Counter64, Integer32, ModuleIdentity, NotificationType, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "TimeTicks", "Counter64", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
series5000, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "series5000")
s5RootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 1, 6, 0))
s5RootMib.setRevisions(('2004-07-20 00:00',))
if mibBuilder.loadTexts: s5RootMib.setLastUpdated('200407200000Z')
if mibBuilder.loadTexts: s5RootMib.setOrganization('Nortel Networks')
s5reg = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 1))
s5Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2))
s5EthTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1))
s5TokTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 2))
s5FddTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 3))
s5ChaTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4))
s5ComTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 5))
s5EcellTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 6))
atmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 7))
remoteLoginTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 8))
stpChangeTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 9))
s5Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3))
s5Agent = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 4))
s5Com = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 5))
s5Eth = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 6))
s5Tok = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 7))
s5Fddi = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 8))
s5EnTop = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 9))
s5TrTop = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 10))
s5FdTop = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 11))
s5EnMsTop = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 13))
s5AtmTop = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 14))
s5IfExt = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 15))
bnLogMsg = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 16))
s5Tcs = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 17))
mibBuilder.exportSymbols("S5-ROOT-MIB", s5EcellTrap=s5EcellTrap, s5reg=s5reg, s5EthTrap=s5EthTrap, PYSNMP_MODULE_ID=s5RootMib, s5Tok=s5Tok, s5EnMsTop=s5EnMsTop, s5Chassis=s5Chassis, s5IfExt=s5IfExt, s5ChaTrap=s5ChaTrap, stpChangeTrap=stpChangeTrap, s5EnTop=s5EnTop, s5ComTrap=s5ComTrap, remoteLoginTrap=remoteLoginTrap, s5FddTrap=s5FddTrap, s5Traps=s5Traps, s5Fddi=s5Fddi, s5TrTop=s5TrTop, bnLogMsg=bnLogMsg, s5AtmTop=s5AtmTop, s5Com=s5Com, s5Eth=s5Eth, s5Tcs=s5Tcs, s5TokTrap=s5TokTrap, atmTraps=atmTraps, s5Agent=s5Agent, s5RootMib=s5RootMib, s5FdTop=s5FdTop)