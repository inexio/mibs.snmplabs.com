#
# PySNMP MIB module HP-ICF-IPV6-RA-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-IPV6-RA-GUARD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:34:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Gauge32, Counter64, IpAddress, TimeTicks, Integer32, iso, Bits, ObjectIdentity, Unsigned32, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Gauge32", "Counter64", "IpAddress", "TimeTicks", "Integer32", "iso", "Bits", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibIdentifier")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
hpicfIpv6RAGuard = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87))
hpicfIpv6RAGuard.setRevisions(('2011-03-16 05:24',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfIpv6RAGuard.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: hpicfIpv6RAGuard.setLastUpdated('201103160524Z')
if mibBuilder.loadTexts: hpicfIpv6RAGuard.setOrganization('Hewlett-Packard Company HP Networking')
if mibBuilder.loadTexts: hpicfIpv6RAGuard.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfIpv6RAGuard.setDescription('This MIB module contains HP proprietary objects for managing RA Guard.')
hpicfIpv6RAGuardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1))
hpicfIpv6RAGuardConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1))
hpicfRAGuardPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfRAGuardPortTable.setStatus('current')
if mibBuilder.loadTexts: hpicfRAGuardPortTable.setDescription('Per-interface configuration for RA Guard. Ra Guard is used to block IPv6 router advertisements and ICMPv6 router redirects. The log option is to enable debug logging for troubleshooting. It uses a lot of CPU and should be used only for short periods of time. To display debug logging, use debug security ra-guard command.')
hpicfRAGuardPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfRAGuardPortEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfRAGuardPortEntry.setDescription('RA Guard configuration information for a single port.')
hpicfRAGuardPortBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfRAGuardPortBlocked.setStatus('current')
if mibBuilder.loadTexts: hpicfRAGuardPortBlocked.setDescription('This object indicates whether this port is blocked for Router Advertisements and Redirects.')
hpicfRAGuardPortBlockedRAs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfRAGuardPortBlockedRAs.setStatus('current')
if mibBuilder.loadTexts: hpicfRAGuardPortBlockedRAs.setDescription('This number of Router Advertisements blocked for the port.')
hpicfRAGuardPortBlockedRedirs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfRAGuardPortBlockedRedirs.setStatus('current')
if mibBuilder.loadTexts: hpicfRAGuardPortBlockedRedirs.setDescription('This number of Router Redirects blocked for the port.')
hpicfRAGuardPortLog = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfRAGuardPortLog.setStatus('current')
if mibBuilder.loadTexts: hpicfRAGuardPortLog.setDescription('Whether to log RAs and Redirects for the port. The log option is to enable debug logging for troubleshooting. It uses a lot of CPU and should be used only for short periods of time.')
hpicfRAGuardLastErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noError", 1), ("insufficientHardwareResources", 2), ("genericError", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfRAGuardLastErrorCode.setStatus('current')
if mibBuilder.loadTexts: hpicfRAGuardLastErrorCode.setDescription('Error code of the last error that occurred. A non-zero value indicates that the last operation performed by this instance did not succeed.')
hpicfIpv6RAGuardConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2))
hpicfIpv6RAGuardCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 1))
hpicfIpv6RAGuardGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 2))
hpicfIpv6RAGuardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 2, 1)).setObjects(("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortBlocked"), ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortBlockedRAs"), ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortBlockedRedirs"), ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortLog"), ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardLastErrorCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfIpv6RAGuardGroup = hpicfIpv6RAGuardGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfIpv6RAGuardGroup.setDescription('A collection of objects providing configuration for Ipv6 RA Guard.')
hpicfIpv6RAGuardCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 1, 1)).setObjects(("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfIpv6RAGuardGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfIpv6RAGuardCompliance = hpicfIpv6RAGuardCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfIpv6RAGuardCompliance.setDescription('The compliance statement for devices support of HP-ICF-IPV6-RA-GUARD-MIB.')
mibBuilder.exportSymbols("HP-ICF-IPV6-RA-GUARD-MIB", hpicfIpv6RAGuardConfig=hpicfIpv6RAGuardConfig, hpicfRAGuardPortLog=hpicfRAGuardPortLog, hpicfIpv6RAGuardCompliances=hpicfIpv6RAGuardCompliances, hpicfIpv6RAGuardGroup=hpicfIpv6RAGuardGroup, hpicfIpv6RAGuardCompliance=hpicfIpv6RAGuardCompliance, hpicfRAGuardPortEntry=hpicfRAGuardPortEntry, hpicfIpv6RAGuardObjects=hpicfIpv6RAGuardObjects, PYSNMP_MODULE_ID=hpicfIpv6RAGuard, hpicfRAGuardPortBlocked=hpicfRAGuardPortBlocked, hpicfRAGuardPortTable=hpicfRAGuardPortTable, hpicfRAGuardPortBlockedRAs=hpicfRAGuardPortBlockedRAs, hpicfRAGuardPortBlockedRedirs=hpicfRAGuardPortBlockedRedirs, hpicfRAGuardLastErrorCode=hpicfRAGuardLastErrorCode, hpicfIpv6RAGuardConformance=hpicfIpv6RAGuardConformance, hpicfIpv6RAGuardGroups=hpicfIpv6RAGuardGroups, hpicfIpv6RAGuard=hpicfIpv6RAGuard)
