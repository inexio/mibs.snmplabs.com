#
# PySNMP MIB module RADLAN-ENDOFMIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-ENDOFMIB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:46:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Gauge32, ObjectIdentity, Integer32, Counter32, IpAddress, iso, Unsigned32, MibIdentifier, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Gauge32", "ObjectIdentity", "Integer32", "Counter32", "IpAddress", "iso", "Unsigned32", "MibIdentifier", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rndEndOfMibGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 1000))
rndEndOfMibGroup.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rndEndOfMibGroup.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rndEndOfMibGroup.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rndEndOfMibGroup.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
if mibBuilder.loadTexts: rndEndOfMibGroup.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rndEndOfMibGroup.setDescription('This private MIB module defines End of MIB private MIBs.')
rndEndOfMib = MibScalar((1, 3, 6, 1, 4, 1, 89, 1000, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndEndOfMib.setStatus('current')
if mibBuilder.loadTexts: rndEndOfMib.setDescription(' This variable indicates this is the end of RND MIB.')
mibBuilder.exportSymbols("RADLAN-ENDOFMIB-MIB", PYSNMP_MODULE_ID=rndEndOfMibGroup, rndEndOfMibGroup=rndEndOfMibGroup, rndEndOfMib=rndEndOfMib)
