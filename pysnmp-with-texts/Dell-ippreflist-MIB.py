#
# PySNMP MIB module Dell-ippreflist-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-ippreflist-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:57:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
InetAddress, InetZoneIndex, InetVersion, InetAddressPrefixLength, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetZoneIndex", "InetVersion", "InetAddressPrefixLength", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, TimeTicks, iso, Integer32, ModuleIdentity, Unsigned32, Bits, Gauge32, ObjectIdentity, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "TimeTicks", "iso", "Integer32", "ModuleIdentity", "Unsigned32", "Bits", "Gauge32", "ObjectIdentity", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TimeStamp, TextualConvention, TruthValue, DisplayString, RowStatus, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "TruthValue", "DisplayString", "RowStatus", "DateAndTime")
rlIpPrefList = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 212))
class RlIpPrefListEntryType(TextualConvention, Integer32):
    description = 'Prefix List entry type defines data type in the entry. Rule (1) means the entry inludes classification and action. Description (2) means the entry icludes comments only.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rule", 1), ("description", 2))

class RlIpPrefListActionType(TextualConvention, Integer32):
    description = 'Prefix List action type. Drop action prevents packet forwarding. Permit action allows packet forwarding.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("drop", 1), ("permit", 2))

class RlIpPrefListType(TextualConvention, Integer32):
    description = 'Classification type is used to create prefix list rule. IPv4 type means match IPv4 packets. IPv6 type means match IPv6 packets.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

rlIpPrefListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 212, 1), )
if mibBuilder.loadTexts: rlIpPrefListTable.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListTable.setDescription('The IP Prefix List table.')
rlIpPrefListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 212, 1, 1), ).setIndexNames((0, "Dell-ippreflist-MIB", "rlIpPrefListType"), (0, "Dell-ippreflist-MIB", "rlIpPrefListName"), (0, "Dell-ippreflist-MIB", "rlIpPrefListEntryIndex"))
if mibBuilder.loadTexts: rlIpPrefListEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListEntry.setDescription('An entry in the rlIpPrefListTable.')
rlIpPrefListType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 1), RlIpPrefListType())
if mibBuilder.loadTexts: rlIpPrefListType.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListType.setDescription('Prefix List Type.')
rlIpPrefListName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlIpPrefListName.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListName.setDescription('Prefix List Name.')
rlIpPrefListEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967294)))
if mibBuilder.loadTexts: rlIpPrefListEntryIndex.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListEntryIndex.setDescription('Entry Index for specific prefix list.')
rlIpPrefListEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 4), RlIpPrefListEntryType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListEntryType.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListEntryType.setDescription('Prefix list entry type.')
rlIpPrefListInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 5), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListInetAddrType.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListInetAddrType.setDescription('The address type of rlIpPrefListIpAddr.')
rlIpPrefListInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListInetAddr.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListInetAddr.setDescription('IP address.')
rlIpPrefListPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListPrefixLength.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListPrefixLength.setDescription('The prefix list can be a number from 0 to 32 for IPv4 address and from 0 to 128 for IPv6 address.')
rlIpPrefListAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 8), RlIpPrefListActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListAction.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListAction.setDescription('Drop or permit action for a matching condition.')
rlIpPrefListGeLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListGeLength.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListGeLength.setDescription('Specifies the lesser value of a range by applying the ge-length argument to the specified range. ge-length repesents the minimum prefix length to be matched.')
rlIpPrefListLeLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListLeLength.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListLeLength.setDescription('Specifies the greater value of a range by applying the ge-length argument to the specified range. le-length repesents the maximum prefix length to be matched.')
rlIpPrefListDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListDescription.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListDescription.setDescription('Prefix List Name.')
rlIpPrefListHitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 12), Integer32())
if mibBuilder.loadTexts: rlIpPrefListHitCount.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListHitCount.setDescription('Match counter.')
rlIpPrefListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 13), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListRowStatus.setDescription('Row status.')
rlIpPrefListInfoTable = MibTable((1, 3, 6, 1, 4, 1, 89, 212, 2), )
if mibBuilder.loadTexts: rlIpPrefListInfoTable.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListInfoTable.setDescription('The IP Prefix List Info table.')
rlIpPrefListInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 212, 2, 1), ).setIndexNames((0, "Dell-ippreflist-MIB", "rlIpPrefListInfoType"), (0, "Dell-ippreflist-MIB", "rlIpPrefListInfoName"))
if mibBuilder.loadTexts: rlIpPrefListInfoEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListInfoEntry.setDescription('An entry in the rlIpPrefListInfoTable.')
rlIpPrefListInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 2, 1, 1), RlIpPrefListType())
if mibBuilder.loadTexts: rlIpPrefListInfoType.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListInfoType.setDescription('Prefix List Type.')
rlIpPrefListInfoName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlIpPrefListInfoName.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListInfoName.setDescription('Prefix List Name.')
rlIpPrefListInfoEntriesNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpPrefListInfoEntriesNumber.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListInfoEntriesNumber.setDescription('Number of entries for specific prefix list.')
rlIpPrefListInfoRangeEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpPrefListInfoRangeEntries.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListInfoRangeEntries.setDescription('Number of entries with range for specific prefix list.')
rlIpPrefListInfoNextFreeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 212, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpPrefListInfoNextFreeIndex.setStatus('current')
if mibBuilder.loadTexts: rlIpPrefListInfoNextFreeIndex.setDescription('Next free index for specific prefix list.')
mibBuilder.exportSymbols("Dell-ippreflist-MIB", rlIpPrefListTable=rlIpPrefListTable, rlIpPrefListInfoName=rlIpPrefListInfoName, rlIpPrefListInfoNextFreeIndex=rlIpPrefListInfoNextFreeIndex, rlIpPrefListInfoType=rlIpPrefListInfoType, rlIpPrefListEntry=rlIpPrefListEntry, rlIpPrefListInfoEntriesNumber=rlIpPrefListInfoEntriesNumber, rlIpPrefListInfoTable=rlIpPrefListInfoTable, rlIpPrefListEntryIndex=rlIpPrefListEntryIndex, rlIpPrefListInfoEntry=rlIpPrefListInfoEntry, rlIpPrefListLeLength=rlIpPrefListLeLength, rlIpPrefListAction=rlIpPrefListAction, rlIpPrefListHitCount=rlIpPrefListHitCount, rlIpPrefListInfoRangeEntries=rlIpPrefListInfoRangeEntries, RlIpPrefListEntryType=RlIpPrefListEntryType, rlIpPrefListInetAddr=rlIpPrefListInetAddr, rlIpPrefListInetAddrType=rlIpPrefListInetAddrType, rlIpPrefListEntryType=rlIpPrefListEntryType, rlIpPrefListType=rlIpPrefListType, rlIpPrefListGeLength=rlIpPrefListGeLength, RlIpPrefListType=RlIpPrefListType, rlIpPrefListPrefixLength=rlIpPrefListPrefixLength, RlIpPrefListActionType=RlIpPrefListActionType, rlIpPrefListDescription=rlIpPrefListDescription, rlIpPrefListRowStatus=rlIpPrefListRowStatus, rlIpPrefList=rlIpPrefList, rlIpPrefListName=rlIpPrefListName)
