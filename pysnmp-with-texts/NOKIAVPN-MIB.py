#
# PySNMP MIB module NOKIAVPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIAVPN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
nokiaVPN, = mibBuilder.importSymbols("NOKIA-OID-REGISTRATION-MIB", "nokiaVPN")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Integer32, Counter32, Counter64, Gauge32, iso, ModuleIdentity, enterprises, Bits, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Integer32", "Counter32", "Counter64", "Gauge32", "iso", "ModuleIdentity", "enterprises", "Bits", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nokiaVPNProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1))
if mibBuilder.loadTexts: nokiaVPNProducts.setStatus('current')
if mibBuilder.loadTexts: nokiaVPNProducts.setDescription('Products')
nokiaVPNMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 2))
if mibBuilder.loadTexts: nokiaVPNMgmt.setStatus('current')
if mibBuilder.loadTexts: nokiaVPNMgmt.setDescription('Management')
nokiaVPNExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 3))
if mibBuilder.loadTexts: nokiaVPNExperiment.setStatus('current')
if mibBuilder.loadTexts: nokiaVPNExperiment.setDescription('Experiment provides a root object identifier from which experimental mibs may be temporarily based. mibs are typicially based here if they fall in one of two categories 1) are IETF work-in-process mibs which have not been assigned a permanent object identifier by the IANA. 2) are Network Alchemy work-in-process which has not been assigned a permanent object identifier by the Network Alchemy assigned number authority, typicially because the MIB is not ready for deployment. NOTE WELL: support for MIBs in the nokiaVPNExperiment subtree will be deleted when a permanent object identifier assignment is made.')
nokiaVPNAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 4))
if mibBuilder.loadTexts: nokiaVPNAdmin.setStatus('current')
if mibBuilder.loadTexts: nokiaVPNAdmin.setDescription('Reserved for administratively assigned OBJECT IDENTIFIERS, i.e. those not associated with MIB objects')
nokiaVPNModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 5))
if mibBuilder.loadTexts: nokiaVPNModules.setStatus('current')
if mibBuilder.loadTexts: nokiaVPNModules.setDescription('Provides a root object identifier from which MODULE-IDENTITY values may be assigned.')
nokiaVPNTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 6))
if mibBuilder.loadTexts: nokiaVPNTraps.setStatus('current')
if mibBuilder.loadTexts: nokiaVPNTraps.setDescription('All the traps common to Nokia VPN fall under here.')
ipsec = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1))
if mibBuilder.loadTexts: ipsec.setStatus('current')
if mibBuilder.loadTexts: ipsec.setDescription('IPSEC (statistics) MIB')
vpn = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2))
if mibBuilder.loadTexts: vpn.setStatus('current')
if mibBuilder.loadTexts: vpn.setDescription('VPN (L2TP/PPTP tunnel statistics) MIB')
config = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3))
if mibBuilder.loadTexts: config.setStatus('current')
if mibBuilder.loadTexts: config.setDescription('General configuration MIB')
nokiaHardwareUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 1))
if mibBuilder.loadTexts: nokiaHardwareUnknown.setStatus('current')
if mibBuilder.loadTexts: nokiaHardwareUnknown.setDescription('Unknown hardware.')
nokiaCryptoCluster500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 4))
if mibBuilder.loadTexts: nokiaCryptoCluster500.setStatus('current')
if mibBuilder.loadTexts: nokiaCryptoCluster500.setDescription('CryptoCluster 500.')
nokiaCryptoCluster5010 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 5))
if mibBuilder.loadTexts: nokiaCryptoCluster5010.setStatus('current')
if mibBuilder.loadTexts: nokiaCryptoCluster5010.setDescription('CryptoCluster 5010.')
nokiaCryptoCluster501 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 8))
if mibBuilder.loadTexts: nokiaCryptoCluster501.setStatus('current')
if mibBuilder.loadTexts: nokiaCryptoCluster501.setDescription('CryptoCluster 501.')
nokiaCryptoCluster5000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 10))
if mibBuilder.loadTexts: nokiaCryptoCluster5000.setStatus('current')
if mibBuilder.loadTexts: nokiaCryptoCluster5000.setDescription('CryptoCluster 5000.')
nokiaCryptoCluster2500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 11))
if mibBuilder.loadTexts: nokiaCryptoCluster2500.setStatus('current')
if mibBuilder.loadTexts: nokiaCryptoCluster2500.setDescription('CryptoCluster 2500.')
nokiaCryptoCluster2501 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 12))
if mibBuilder.loadTexts: nokiaCryptoCluster2501.setStatus('current')
if mibBuilder.loadTexts: nokiaCryptoCluster2501.setDescription('CryptoCluster 2501.')
nokiaCryptoCluster5200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 15))
if mibBuilder.loadTexts: nokiaCryptoCluster5200.setStatus('current')
if mibBuilder.loadTexts: nokiaCryptoCluster5200.setDescription('CryptoCluster 5200.')
nokiaCryptoCluster5205 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 16))
if mibBuilder.loadTexts: nokiaCryptoCluster5205.setStatus('current')
if mibBuilder.loadTexts: nokiaCryptoCluster5205.setDescription('CryptoCluster 5205.')
nokiaCA200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 18))
if mibBuilder.loadTexts: nokiaCA200.setStatus('current')
if mibBuilder.loadTexts: nokiaCA200.setDescription('CA200.')
nokiaCA600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 19))
if mibBuilder.loadTexts: nokiaCA600.setStatus('current')
if mibBuilder.loadTexts: nokiaCA600.setDescription('CA600.')
nokiaCryptoCluster100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 20))
if mibBuilder.loadTexts: nokiaCryptoCluster100.setStatus('current')
if mibBuilder.loadTexts: nokiaCryptoCluster100.setDescription('CryptoCluster.')
mibBuilder.exportSymbols("NOKIAVPN-MIB", nokiaCA200=nokiaCA200, nokiaCryptoCluster100=nokiaCryptoCluster100, nokiaCryptoCluster2501=nokiaCryptoCluster2501, ipsec=ipsec, nokiaVPNAdmin=nokiaVPNAdmin, nokiaVPNExperiment=nokiaVPNExperiment, nokiaVPNProducts=nokiaVPNProducts, nokiaVPNMgmt=nokiaVPNMgmt, nokiaHardwareUnknown=nokiaHardwareUnknown, nokiaCryptoCluster5205=nokiaCryptoCluster5205, nokiaCA600=nokiaCA600, nokiaCryptoCluster5200=nokiaCryptoCluster5200, config=config, nokiaCryptoCluster500=nokiaCryptoCluster500, nokiaVPNModules=nokiaVPNModules, nokiaCryptoCluster5010=nokiaCryptoCluster5010, nokiaCryptoCluster501=nokiaCryptoCluster501, vpn=vpn, nokiaCryptoCluster5000=nokiaCryptoCluster5000, nokiaVPNTraps=nokiaVPNTraps, nokiaCryptoCluster2500=nokiaCryptoCluster2500)