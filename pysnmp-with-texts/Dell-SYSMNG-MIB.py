#
# PySNMP MIB module Dell-SYSMNG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-SYSMNG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:56:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rnd, Percents = mibBuilder.importSymbols("Dell-MIB", "rnd", "Percents")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, ObjectIdentity, NotificationType, Unsigned32, IpAddress, MibIdentifier, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Counter64", "Bits")
DisplayString, RowPointer, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowPointer", "TruthValue", "RowStatus", "TextualConvention")
rlSysmngMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 204))
rlSysmngMib.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSysmngMib.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlSysmngMib.setLastUpdated('201010310000a')
if mibBuilder.loadTexts: rlSysmngMib.setOrganization('Dell')
if mibBuilder.loadTexts: rlSysmngMib.setContactInfo('Dell.com')
if mibBuilder.loadTexts: rlSysmngMib.setDescription('The private MIB module definition for System Manager pool.')
class SysmngResourceRouteType(TextualConvention, Integer32):
    description = 'Supported router resource types'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("ipmv4", 3), ("ipmv6", 4), ("nonIp", 5))

class SysmngResourceRouteUsageType(TextualConvention, Integer32):
    description = 'Supported router resource usage types'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("ipv4Neighbor", 1), ("ipv4Address", 2), ("ipv4Route", 3), ("ipv6Neighbor", 4), ("ipv6Address", 5), ("ipv6OnlinkPrefix", 6), ("ipv6Route", 7), ("ipmv4Route", 8), ("ipmv4RouteStarG", 9), ("ipmv6Route", 10), ("ipmv6RouteStarG", 11))

class SysmngPoolType(TextualConvention, Integer32):
    description = 'Supported TCAM pools.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("router", 1), ("iscsi", 2), ("voip", 3), ("misc", 4))

rlSysmngTcamAllocations = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 204, 1))
rlSysmngTcamAllocationsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 204, 1, 1), )
if mibBuilder.loadTexts: rlSysmngTcamAllocationsTable.setStatus('current')
if mibBuilder.loadTexts: rlSysmngTcamAllocationsTable.setDescription('A table containing tcam allocations information. Each row represents objects for a defined profile.')
rlSysmngTcamAllocationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 204, 1, 1, 1), ).setIndexNames((0, "Dell-SYSMNG-MIB", "rlSysmngTcamAllocProfileName"), (0, "Dell-SYSMNG-MIB", "rlSysmngTcamAllocPoolType"))
if mibBuilder.loadTexts: rlSysmngTcamAllocationsEntry.setStatus('current')
if mibBuilder.loadTexts: rlSysmngTcamAllocationsEntry.setDescription('A Single entry containing tcam allocations information per predefined profile and specific pool.')
rlSysmngTcamAllocProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 1, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: rlSysmngTcamAllocProfileName.setStatus('current')
if mibBuilder.loadTexts: rlSysmngTcamAllocProfileName.setDescription("The profile name for tcam allocation. Must be unique per entry. This is an index into the table. 'tcam0' profile contains policy tcam counters 'tcam1' profile contains router tcam counters")
rlSysmngTcamAllocPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 1, 1, 1, 2), SysmngPoolType())
if mibBuilder.loadTexts: rlSysmngTcamAllocPoolType.setStatus('current')
if mibBuilder.loadTexts: rlSysmngTcamAllocPoolType.setDescription('Pool type. Must be unique per entry. This is an index into the table.')
rlSysmngTcamAllocMinRequiredEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngTcamAllocMinRequiredEntries.setStatus('current')
if mibBuilder.loadTexts: rlSysmngTcamAllocMinRequiredEntries.setDescription('Number of minimal hardware entries, required by pool to operate.')
rlSysmngTcamAllocStaticConfigEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngTcamAllocStaticConfigEntries.setStatus('current')
if mibBuilder.loadTexts: rlSysmngTcamAllocStaticConfigEntries.setDescription('Number of hardware entries, in use by static configuration of the pool.')
rlSysmngTcamAllocInUseEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngTcamAllocInUseEntries.setStatus('current')
if mibBuilder.loadTexts: rlSysmngTcamAllocInUseEntries.setDescription('Total number of hardware entries, currently in use by the pool. This number includes minimum, static and dynamic entries.')
rlSysmngTcamAllocPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngTcamAllocPoolSize.setStatus('current')
if mibBuilder.loadTexts: rlSysmngTcamAllocPoolSize.setDescription('Total number of hardware entries reserved for the pool.')
rlSysmngResource = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 204, 2))
rlSysmngResourceTable = MibTable((1, 3, 6, 1, 4, 1, 89, 204, 2, 1), )
if mibBuilder.loadTexts: rlSysmngResourceTable.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceTable.setDescription('A read-only table for displaying router resources configuration, properties, and usage per resource.')
rlSysmngResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 204, 2, 1, 1), ).setIndexNames((0, "Dell-SYSMNG-MIB", "rlSysmngResourceRouteType"))
if mibBuilder.loadTexts: rlSysmngResourceEntry.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceEntry.setDescription('A Single entry containing specific router resource information.')
rlSysmngResourceRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 2, 1, 1, 1), SysmngResourceRouteType())
if mibBuilder.loadTexts: rlSysmngResourceRouteType.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceRouteType.setDescription('Router resource type.')
rlSysmngResourceCurrentUse = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentUse.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceCurrentUse.setDescription('Currently in used number of routes.')
rlSysmngResourceCurrentUseHw = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentUseHw.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceCurrentUseHw.setDescription('Currently in used number of HW FFT entries')
rlSysmngResourceCurrentMax = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentMax.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceCurrentMax.setDescription('The running maximum supported number of routes.')
rlSysmngResourceCurrentMaxHw = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentMaxHw.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceCurrentMaxHw.setDescription('The running maximum supported number of HW FFT entries.')
rlSysmngResourceTemporaryMax = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceTemporaryMax.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceTemporaryMax.setDescription('The temporary maximum supported number of routes.')
rlSysmngResourceTemporaryMaxHw = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceTemporaryMaxHw.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceTemporaryMaxHw.setDescription('The temporary maximum supported number of HW FFT entries.')
rlSysmngResourceCurrentNexthopMax = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentNexthopMax.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceCurrentNexthopMax.setDescription('The maximum supported number of nexthop entries.')
rlSysmngResourceCurrentNexthopMaxHw = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentNexthopMaxHw.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceCurrentNexthopMaxHw.setDescription('The maximum supported number of HW nexthop entries.')
rlSysmngResourceCurrentNexthopUse = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentNexthopUse.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceCurrentNexthopUse.setDescription('The current number of nexthop entries.')
rlSysmngResourceCurrentNexthopUseHw = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentNexthopUseHw.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceCurrentNexthopUseHw.setDescription('The current number of HW nexthop entries.')
rlSysmngRouterResourceAction = MibScalar((1, 3, 6, 1, 4, 1, 89, 204, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSysmngRouterResourceAction.setStatus('current')
if mibBuilder.loadTexts: rlSysmngRouterResourceAction.setDescription('Router recource action.')
rlSysmngResourceUsage = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 204, 4))
rlSysmngResourceUsageTable = MibTable((1, 3, 6, 1, 4, 1, 89, 204, 4, 1), )
if mibBuilder.loadTexts: rlSysmngResourceUsageTable.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceUsageTable.setDescription('A read-only table for displaying router resources configuration, properties, and usage per resource.')
rlSysmngResourceUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 204, 4, 1, 1), ).setIndexNames((0, "Dell-SYSMNG-MIB", "rlSysmngResourceUsageType"))
if mibBuilder.loadTexts: rlSysmngResourceUsageEntry.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceUsageEntry.setDescription('A Single entry containing specific router resource information.')
rlSysmngResourceUsageType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 4, 1, 1, 1), SysmngResourceRouteUsageType())
if mibBuilder.loadTexts: rlSysmngResourceUsageType.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceUsageType.setDescription('Router resource type.')
rlSysmngResourceUsageNum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceUsageNum.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourceUsageNum.setDescription('Currently in used.')
rlSysmngResourcePerUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 204, 5))
rlSysmngResourcePerUnitTable = MibTable((1, 3, 6, 1, 4, 1, 89, 204, 5, 1), )
if mibBuilder.loadTexts: rlSysmngResourcePerUnitTable.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitTable.setDescription('A read-only table for displaying router resources configuration, properties, and usage per resource.')
rlSysmngResourcePerUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1), ).setIndexNames((0, "Dell-SYSMNG-MIB", "rlSysmngResourcePerUnitRouteType"), (0, "Dell-SYSMNG-MIB", "rlSysmngResourcePerUnitUnitId"))
if mibBuilder.loadTexts: rlSysmngResourcePerUnitEntry.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitEntry.setDescription('A Single entry containing specific router resource information.')
rlSysmngResourcePerUnitRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1, 1), SysmngResourceRouteType())
if mibBuilder.loadTexts: rlSysmngResourcePerUnitRouteType.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitRouteType.setDescription('Router resource type.')
rlSysmngResourcePerUnitUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: rlSysmngResourcePerUnitUnitId.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitUnitId.setDescription('Unit id. Zero value means system totals.')
rlSysmngResourcePerUnitCurrentUse = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentUse.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentUse.setDescription('Currently in used number of routes.')
rlSysmngResourcePerUnitCurrentUseHw = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentUseHw.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentUseHw.setDescription('Currently in used number of HW FFT entries')
rlSysmngResourcePerUnitCurrentMax = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentMax.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentMax.setDescription('The running maximum supported number of routes.')
rlSysmngResourcePerUnitCurrentMaxHw = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentMaxHw.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentMaxHw.setDescription('The running maximum supported number of HW FFT entries.')
rlSysmngResourcePerUnitTemporaryMax = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitTemporaryMax.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitTemporaryMax.setDescription('The temporary maximum supported number of routes.')
rlSysmngResourcePerUnitTemporaryMaxHw = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitTemporaryMaxHw.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitTemporaryMaxHw.setDescription('The temporary maximum supported number of HW FFT entries.')
rlSysmngResourcePerUnitCurrentNexthopMax = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentNexthopMax.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentNexthopMax.setDescription('The maximum supported number of nexthop entries.')
rlSysmngResourcePerUnitCurrentNexthopMaxHw = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentNexthopMaxHw.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentNexthopMaxHw.setDescription('The maximum supported number of HW nexthop entries.')
rlSysmngResourcePerUnitCurrentNexthopUse = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentNexthopUse.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentNexthopUse.setDescription('The current number of nexthop entries.')
rlSysmngResourcePerUnitCurrentNexthopUseHw = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 204, 5, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentNexthopUseHw.setStatus('current')
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentNexthopUseHw.setDescription('The current number of HW nexthop entries.')
mibBuilder.exportSymbols("Dell-SYSMNG-MIB", rlSysmngResourceUsageType=rlSysmngResourceUsageType, rlSysmngResourceCurrentNexthopUseHw=rlSysmngResourceCurrentNexthopUseHw, rlSysmngMib=rlSysmngMib, rlSysmngTcamAllocationsTable=rlSysmngTcamAllocationsTable, rlSysmngResourcePerUnitCurrentNexthopMax=rlSysmngResourcePerUnitCurrentNexthopMax, rlSysmngResourceCurrentNexthopMaxHw=rlSysmngResourceCurrentNexthopMaxHw, rlSysmngResourcePerUnitCurrentNexthopUse=rlSysmngResourcePerUnitCurrentNexthopUse, rlSysmngTcamAllocInUseEntries=rlSysmngTcamAllocInUseEntries, rlSysmngResourceRouteType=rlSysmngResourceRouteType, rlSysmngResourcePerUnitCurrentMax=rlSysmngResourcePerUnitCurrentMax, rlSysmngResource=rlSysmngResource, rlSysmngTcamAllocPoolType=rlSysmngTcamAllocPoolType, rlSysmngResourceTemporaryMaxHw=rlSysmngResourceTemporaryMaxHw, rlSysmngResourceTable=rlSysmngResourceTable, rlSysmngResourceCurrentUseHw=rlSysmngResourceCurrentUseHw, rlSysmngResourcePerUnitCurrentNexthopUseHw=rlSysmngResourcePerUnitCurrentNexthopUseHw, rlSysmngTcamAllocationsEntry=rlSysmngTcamAllocationsEntry, rlSysmngResourcePerUnit=rlSysmngResourcePerUnit, rlSysmngResourcePerUnitTable=rlSysmngResourcePerUnitTable, rlSysmngResourceCurrentMax=rlSysmngResourceCurrentMax, rlSysmngResourcePerUnitCurrentUseHw=rlSysmngResourcePerUnitCurrentUseHw, rlSysmngResourcePerUnitUnitId=rlSysmngResourcePerUnitUnitId, rlSysmngResourcePerUnitCurrentUse=rlSysmngResourcePerUnitCurrentUse, rlSysmngTcamAllocProfileName=rlSysmngTcamAllocProfileName, rlSysmngTcamAllocMinRequiredEntries=rlSysmngTcamAllocMinRequiredEntries, rlSysmngResourceCurrentNexthopMax=rlSysmngResourceCurrentNexthopMax, rlSysmngResourcePerUnitCurrentMaxHw=rlSysmngResourcePerUnitCurrentMaxHw, rlSysmngTcamAllocations=rlSysmngTcamAllocations, rlSysmngResourcePerUnitEntry=rlSysmngResourcePerUnitEntry, rlSysmngResourceTemporaryMax=rlSysmngResourceTemporaryMax, rlSysmngResourceEntry=rlSysmngResourceEntry, rlSysmngResourcePerUnitTemporaryMax=rlSysmngResourcePerUnitTemporaryMax, rlSysmngResourcePerUnitRouteType=rlSysmngResourcePerUnitRouteType, rlSysmngRouterResourceAction=rlSysmngRouterResourceAction, PYSNMP_MODULE_ID=rlSysmngMib, rlSysmngResourceUsage=rlSysmngResourceUsage, rlSysmngTcamAllocPoolSize=rlSysmngTcamAllocPoolSize, SysmngPoolType=SysmngPoolType, rlSysmngResourceUsageNum=rlSysmngResourceUsageNum, rlSysmngTcamAllocStaticConfigEntries=rlSysmngTcamAllocStaticConfigEntries, rlSysmngResourceCurrentNexthopUse=rlSysmngResourceCurrentNexthopUse, SysmngResourceRouteUsageType=SysmngResourceRouteUsageType, rlSysmngResourceUsageEntry=rlSysmngResourceUsageEntry, SysmngResourceRouteType=SysmngResourceRouteType, rlSysmngResourceCurrentMaxHw=rlSysmngResourceCurrentMaxHw, rlSysmngResourcePerUnitTemporaryMaxHw=rlSysmngResourcePerUnitTemporaryMaxHw, rlSysmngResourcePerUnitCurrentNexthopMaxHw=rlSysmngResourcePerUnitCurrentNexthopMaxHw, rlSysmngResourceCurrentUse=rlSysmngResourceCurrentUse, rlSysmngResourceUsageTable=rlSysmngResourceUsageTable)
