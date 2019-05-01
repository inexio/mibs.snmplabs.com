#
# PySNMP MIB module NETAL-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETAL-SMI
# Produced by pysmi-0.3.4 at Wed May  1 14:18:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, enterprises, ObjectIdentity, Counter32, Gauge32, NotificationType, Unsigned32, ModuleIdentity, iso, MibIdentifier, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "enterprises", "ObjectIdentity", "Counter32", "Gauge32", "NotificationType", "Unsigned32", "ModuleIdentity", "iso", "MibIdentifier", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
networkAlchemy = ModuleIdentity((1, 3, 6, 1, 4, 1, 2972))
networkAlchemy.setRevisions(('2000-10-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: networkAlchemy.setRevisionsDescriptions(('Cleanup.',))
if mibBuilder.loadTexts: networkAlchemy.setLastUpdated('200010250000Z')
if mibBuilder.loadTexts: networkAlchemy.setOrganization('Network Alchemy, Inc.')
if mibBuilder.loadTexts: networkAlchemy.setContactInfo(' Network Alchemy Customer Support Postal: 1538 Pacific Av. Santa Cruz, CA 95060 USA E-Mail: snmp-contact@network-alchemy.com')
if mibBuilder.loadTexts: networkAlchemy.setDescription('The Structure of Management Information for the Network Alchemy enterprise.')
netalProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1))
if mibBuilder.loadTexts: netalProducts.setStatus('current')
if mibBuilder.loadTexts: netalProducts.setDescription('netalProducts is the root OBJECT IDENTIFIER from which sysObjectID values are assigned. Actual values are defined in the NETAL-PRODUCTS-MIB.')
netalMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 2))
if mibBuilder.loadTexts: netalMgmt.setStatus('current')
if mibBuilder.loadTexts: netalMgmt.setDescription('netalMgmt is the main subtree for new mib development.')
netalExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 3))
if mibBuilder.loadTexts: netalExperiment.setStatus('current')
if mibBuilder.loadTexts: netalExperiment.setDescription('netalExperiment provides a root object identifier from which experimental mibs may be temporarily based. mibs are typicially based here if they fall in one of two categories 1) are IETF work-in-process mibs which have not been assigned a permanent object identifier by the IANA. 2) are Network Alchemy work-in-process which has not been assigned a permanent object identifier by the Network Alchemy assigned number authority, typicially because the MIB is not ready for deployment. NOTE WELL: support for MIBs in the netalExperiment subtree will be deleted when a permanent object identifier assignment is made.')
netalAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 4))
if mibBuilder.loadTexts: netalAdmin.setStatus('current')
if mibBuilder.loadTexts: netalAdmin.setDescription('netalAdmin is reserved for administratively assigned OBJECT IDENTIFIERS, i.e. those not associated with MIB objects')
netalModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 5))
if mibBuilder.loadTexts: netalModules.setStatus('current')
if mibBuilder.loadTexts: netalModules.setDescription('netalModules provides a root object identifier from which MODULE-IDENTITY values may be assigned.')
netalTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 6))
if mibBuilder.loadTexts: netalTraps.setStatus('current')
if mibBuilder.loadTexts: netalTraps.setDescription('All the traps send by and from the Network Alchemy Crypto Cluster fall under here.')
cryptoCluster = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 2, 1))
if mibBuilder.loadTexts: cryptoCluster.setStatus('current')
if mibBuilder.loadTexts: cryptoCluster.setDescription('Crypto Cluster MIB')
ipsec = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 2, 2))
if mibBuilder.loadTexts: ipsec.setStatus('current')
if mibBuilder.loadTexts: ipsec.setDescription('IPSEC MIB')
hardware = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 2, 3))
if mibBuilder.loadTexts: hardware.setStatus('current')
if mibBuilder.loadTexts: hardware.setDescription('Crypto Cluster Hardware MIB')
vpn = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 2, 4))
if mibBuilder.loadTexts: vpn.setStatus('current')
if mibBuilder.loadTexts: vpn.setDescription('Crypto Cluster VPN (tunnel) MIB')
config = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 2, 5))
if mibBuilder.loadTexts: config.setStatus('current')
if mibBuilder.loadTexts: config.setDescription('Configuration administration parameters')
mibBuilder.exportSymbols("NETAL-SMI", hardware=hardware, config=config, ipsec=ipsec, netalExperiment=netalExperiment, PYSNMP_MODULE_ID=networkAlchemy, netalTraps=netalTraps, vpn=vpn, netalAdmin=netalAdmin, netalModules=netalModules, cryptoCluster=cryptoCluster, networkAlchemy=networkAlchemy, netalMgmt=netalMgmt, netalProducts=netalProducts)
