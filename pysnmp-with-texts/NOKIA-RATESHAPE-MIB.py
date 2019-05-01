#
# PySNMP MIB module NOKIA-RATESHAPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-RATESHAPE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, enterprises, MibIdentifier, Unsigned32, Gauge32, Counter64, Counter32, Integer32, iso, NotificationType, ModuleIdentity, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "MibIdentifier", "Unsigned32", "Gauge32", "Counter64", "Counter32", "Integer32", "iso", "NotificationType", "ModuleIdentity", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
ntcRS = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 1, 16, 4))
ntcRS.setRevisions(('1900-01-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntcRS.setRevisionsDescriptions(('Co-Editor: Kripakaran Karlekar Converted MIB from SMIv1 to SMIv2 format',))
if mibBuilder.loadTexts: ntcRS.setLastUpdated('0001300000Z')
if mibBuilder.loadTexts: ntcRS.setOrganization('Nokia')
if mibBuilder.loadTexts: ntcRS.setContactInfo('Alan Fransisco Postal: 313 Fairchild Drive Mountain View, California, 94043')
if mibBuilder.loadTexts: ntcRS.setDescription('This MIB Module defines the Rate Shaping MIB. More detailed description of the variables and tables is provided in other related documentation.')
nokia = MibIdentifier((1, 3, 6, 1, 4, 1, 94))
nokiaProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1))
ntcCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16))
class PacketSource(TextualConvention, Integer32):
    description = ' The source of the packet rate-limited for. input statistics of the input packets. output statistics of the output packets. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("input", 1), ("output", 2))

class RateLimitAction(TextualConvention, Integer32):
    description = ' The action taken after evaluating the rate limit. drop drop the packet. accept transmit the packet. reject discard the packet and return ICMP error message. condition pass to the traffic conditioner. skip inactive rule, must perform default action. prioritize prioritize the packet.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("drop", 1), ("accept", 2), ("reject", 3), ("condition", 4), ("skip", 5), ("prioritize", 6))

rsAccessLists = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1)).setObjects(("NOKIA-RATESHAPE-MIB", "rsAccessListIfIndex"), ("NOKIA-RATESHAPE-MIB", "rsAccessListIndex"), ("NOKIA-RATESHAPE-MIB", "rsAccessListDirection"), ("NOKIA-RATESHAPE-MIB", "rsAccessListName"), ("NOKIA-RATESHAPE-MIB", "rsAccessListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsAccessLists = rsAccessLists.setStatus('current')
if mibBuilder.loadTexts: rsAccessLists.setDescription('A collection of objects providing the instrumentation of rsAccessLists')
rsAccessListTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1), )
if mibBuilder.loadTexts: rsAccessListTable.setStatus('current')
if mibBuilder.loadTexts: rsAccessListTable.setDescription('A table of access list configuration entries. An access list will contain several rules for rate limits which are applied to one or more MIB-II interface-direction tuples. Each MIB-II interface may not utilize more than two access lists; one for the in direction and one for the out direction.')
rsAccessListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1), ).setIndexNames((0, "NOKIA-RATESHAPE-MIB", "rsAccessListIfIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAccessListIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAccessListDirection"))
if mibBuilder.loadTexts: rsAccessListEntry.setStatus('current')
if mibBuilder.loadTexts: rsAccessListEntry.setDescription('A series of objects used to describe each access list.')
rsAccessListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListIfIndex.setStatus('current')
if mibBuilder.loadTexts: rsAccessListIfIndex.setDescription('The ifIndex of the MIB-II interface which this access list entry is responsible for. ')
rsAccessListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListIndex.setStatus('current')
if mibBuilder.loadTexts: rsAccessListIndex.setDescription('A unique index value for this access list.')
rsAccessListDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 3), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListDirection.setStatus('current')
if mibBuilder.loadTexts: rsAccessListDirection.setDescription('The data source for this access list.')
rsAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsAccessListName.setStatus('current')
if mibBuilder.loadTexts: rsAccessListName.setDescription('This string provides a unique descriptor for this access list. If an attempt is made to set this string to the name of another access list on the agent, it should return noSuchName.')
rsAccessListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsAccessListRowStatus.setStatus('current')
if mibBuilder.loadTexts: rsAccessListRowStatus.setDescription("The current status of this access list. Setting this object to 'destroy' has the effect of deleting this access list. createAndGo(4) appends to the list and activates it. ")
rsRules = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2)).setObjects(("NOKIA-RATESHAPE-MIB", "rsRuleIfIndex"), ("NOKIA-RATESHAPE-MIB", "rsRuleIndex"), ("NOKIA-RATESHAPE-MIB", "rsRuleDirection"), ("NOKIA-RATESHAPE-MIB", "rsRuleTOS"), ("NOKIA-RATESHAPE-MIB", "rsRuleAction"), ("NOKIA-RATESHAPE-MIB", "rsRuleSrcAddress"), ("NOKIA-RATESHAPE-MIB", "rsRuleSrcAddrMask"), ("NOKIA-RATESHAPE-MIB", "rsRuleDestAddress"), ("NOKIA-RATESHAPE-MIB", "rsRuleDestAddrMask"), ("NOKIA-RATESHAPE-MIB", "rsRuleIpProtocol"), ("NOKIA-RATESHAPE-MIB", "rsRuleSrcStartingPort"), ("NOKIA-RATESHAPE-MIB", "rsRuleSrcEndingPort"), ("NOKIA-RATESHAPE-MIB", "rsRuleDestStartingPort"), ("NOKIA-RATESHAPE-MIB", "rsRuleDestEndingPort"), ("NOKIA-RATESHAPE-MIB", "rsRuleAggregationClassIndex"), ("NOKIA-RATESHAPE-MIB", "rsRuleEstablished"), ("NOKIA-RATESHAPE-MIB", "rsRuleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRules = rsRules.setStatus('current')
if mibBuilder.loadTexts: rsRules.setDescription('A collection of objects providing the instrumentation of rsRules')
rsRuleTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1), )
if mibBuilder.loadTexts: rsRuleTable.setStatus('current')
if mibBuilder.loadTexts: rsRuleTable.setDescription('A table of rate limit configuration entries. Rate Limit is a method of traffic control. It allows a set of rate limits to be configured and applied to packets flowing into/out of an interface to regulate network traffic.')
rsRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1), ).setIndexNames((0, "NOKIA-RATESHAPE-MIB", "rsRuleIfIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsRuleIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsRuleDirection"))
if mibBuilder.loadTexts: rsRuleEntry.setStatus('current')
if mibBuilder.loadTexts: rsRuleEntry.setDescription('A collection of rate-limit configuration objects on this interface. Entries in the rsRuleTable is created and deleted via the rate-limit command line interface.')
rsRuleIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleIfIndex.setStatus('current')
if mibBuilder.loadTexts: rsRuleIfIndex.setDescription('The ifIndex of the MIB-II interface which this access list entry is responsible for. ')
rsRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleIndex.setStatus('current')
if mibBuilder.loadTexts: rsRuleIndex.setDescription('An arbitrary index for rate limit objects. It will increase as the list for each rsRuleIfIndex is traversed.In other words,the value of rsRuleIndex increments for the same value of rsRuleIfIndex, but starts over at 1 once the value of rsRuleIfIndex changes.')
rsRuleDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 3), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleDirection.setStatus('current')
if mibBuilder.loadTexts: rsRuleDirection.setDescription('The data source for the Rate Limit object.')
rsRuleTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleTOS.setStatus('current')
if mibBuilder.loadTexts: rsRuleTOS.setDescription('The TOS field of the type of packet which this rule governs.')
rsRuleAction = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 5), RateLimitAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleAction.setStatus('current')
if mibBuilder.loadTexts: rsRuleAction.setDescription('The forwarding Action associated with this rule.')
rsRuleSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleSrcAddress.setStatus('current')
if mibBuilder.loadTexts: rsRuleSrcAddress.setDescription('The source IP address for this rule.')
rsRuleSrcAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleSrcAddrMask.setStatus('current')
if mibBuilder.loadTexts: rsRuleSrcAddrMask.setDescription('The mask of source address for this rule.')
rsRuleDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleDestAddress.setStatus('current')
if mibBuilder.loadTexts: rsRuleDestAddress.setDescription('The destination IP address for this rule.')
rsRuleDestAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleDestAddrMask.setStatus('current')
if mibBuilder.loadTexts: rsRuleDestAddrMask.setDescription('The mask of destination address for this rule.')
rsRuleIpProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleIpProtocol.setStatus('current')
if mibBuilder.loadTexts: rsRuleIpProtocol.setDescription('The number of IP protocol that rule applies on.')
rsRuleSrcStartingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleSrcStartingPort.setStatus('current')
if mibBuilder.loadTexts: rsRuleSrcStartingPort.setDescription('The start of the source range of port number(s) of the IP protocol for this rule.')
rsRuleSrcEndingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleSrcEndingPort.setStatus('current')
if mibBuilder.loadTexts: rsRuleSrcEndingPort.setDescription('The end of the source range of port number(s) of the IP protocol for this rule.')
rsRuleDestStartingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleDestStartingPort.setStatus('current')
if mibBuilder.loadTexts: rsRuleDestStartingPort.setDescription('The start of the destination range of port number(s) of the IP protocol for this rule.')
rsRuleDestEndingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleDestEndingPort.setStatus('current')
if mibBuilder.loadTexts: rsRuleDestEndingPort.setDescription('The end of the destination range of port number(s) of the IP protocol for this rule.')
rsRuleAggregationClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleAggregationClassIndex.setStatus('current')
if mibBuilder.loadTexts: rsRuleAggregationClassIndex.setDescription('The index(rsAggregationClassIndex) to the aggregation class(queue) if RateLimitAction is enqueue(3).')
rsRuleEstablished = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("established", 1), ("notEstablished", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleEstablished.setStatus('current')
if mibBuilder.loadTexts: rsRuleEstablished.setDescription("An integer value indicating whether or not this rule is effective on previously-established TCP connections. 'established' will indicate that upon activation of this rule, only previously-established TCP connections will match this rule. 'notEstablished' will indicate that any TCP connection can match this rule. ")
rsRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleRowStatus.setStatus('current')
if mibBuilder.loadTexts: rsRuleRowStatus.setDescription("The current status of this rule. The rules defined in this table is treated as a linked list. By definition rsRuleRowStatus will ensure that there are no orphan rules i.e the linked list is not broken. Setting a rule to 'destroy' has the effect of deleting this rule. createAndGo(4) appends to the list thus ensuring that there are no orphans. ")
rsAggregationClasses = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3)).setObjects(("NOKIA-RATESHAPE-MIB", "rsAggregationClassIfIndex"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassIndex"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassDirection"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassName"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassMeanRate"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassBurstSize"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsAggregationClasses = rsAggregationClasses.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClasses.setDescription('A collection of objects providing the instrumentation of rsAggregationClasses')
rsAggregationClassTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1), )
if mibBuilder.loadTexts: rsAggregationClassTable.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassTable.setDescription('A table of aggregation class entries.')
rsAggregationClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1), ).setIndexNames((0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassIfIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassDirection"))
if mibBuilder.loadTexts: rsAggregationClassEntry.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassEntry.setDescription('A collection of aggregation class objects on this interface-direction tuple. ')
rsAggregationClassIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassIfIndex.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassIfIndex.setDescription('The value of ifIndex which corresponds to the first interface for which this aggregation class handles tokens. ')
rsAggregationClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassIndex.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassIndex.setDescription('The unique row index of this aggregation class(queue).')
rsAggregationClassDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 3), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassDirection.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassDirection.setDescription('The data source for this aggregation class.')
rsAggregationClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsAggregationClassName.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassName.setDescription('A string which uniquely represents this aggregation class.')
rsAggregationClassMeanRate = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsAggregationClassMeanRate.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassMeanRate.setDescription('The peak bandwidth when rsAggregationClassBurstRate and rsAggregationClassBurstDuration are not set. When mean rate and burst duration are set, the mean rate specifies the long-term rate which the packet stream will be shaped to, but the packet stream can burst above that rate for as long as the burst duration specifies with no penalty. The value noSuchName should be returned if an attempt is made to set the value to a rate is higher than the rate available to this aggregation class.')
rsAggregationClassBurstSize = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1500, 150000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsAggregationClassBurstSize.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassBurstSize.setDescription('The Burst size associated with this aggregation class.')
rsAggregationClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsAggregationClassRowStatus.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassRowStatus.setDescription('The current status of this aggregation class. The behavior of this aggregation class upon changing of this object should be analogous to the behavior of a rule when its rsRuleRowStatus is modified.')
rsAccessListStats = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4)).setObjects(("NOKIA-RATESHAPE-MIB", "rsAccessListStatIfIndex"), ("NOKIA-RATESHAPE-MIB", "rsAccessListStatIndex"), ("NOKIA-RATESHAPE-MIB", "rsAccessListStatDirection"), ("NOKIA-RATESHAPE-MIB", "rsAccessListStatPktsPassed"), ("NOKIA-RATESHAPE-MIB", "rsAccessListStatBytesPassed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsAccessListStats = rsAccessListStats.setStatus('current')
if mibBuilder.loadTexts: rsAccessListStats.setDescription('A collection of objects providing the instrumentation of rsAccessListStats')
rsAccessListStatTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1), )
if mibBuilder.loadTexts: rsAccessListStatTable.setStatus('current')
if mibBuilder.loadTexts: rsAccessListStatTable.setDescription('A table of access list status entries.')
rsAccessListStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1), ).setIndexNames((0, "NOKIA-RATESHAPE-MIB", "rsAccessListStatIfIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAccessListStatIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAccessListStatDirection"))
if mibBuilder.loadTexts: rsAccessListStatEntry.setStatus('current')
if mibBuilder.loadTexts: rsAccessListStatEntry.setDescription('A series of status objects used to describe each access list. ')
rsAccessListStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListStatIfIndex.setStatus('current')
if mibBuilder.loadTexts: rsAccessListStatIfIndex.setDescription('The ifIndex of the MIB-II interface which this access list stat entry is responsible for. ')
rsAccessListStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListStatIndex.setStatus('current')
if mibBuilder.loadTexts: rsAccessListStatIndex.setDescription('A unique index value for this access list.')
rsAccessListStatDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 3), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListStatDirection.setStatus('current')
if mibBuilder.loadTexts: rsAccessListStatDirection.setDescription('The data source for this access list.')
rsAccessListStatPktsPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListStatPktsPassed.setStatus('current')
if mibBuilder.loadTexts: rsAccessListStatPktsPassed.setDescription('Gives the count of number of packets successfully exiting this access list.')
rsAccessListStatBytesPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListStatBytesPassed.setStatus('current')
if mibBuilder.loadTexts: rsAccessListStatBytesPassed.setDescription('Gives the count of number of bytes successfully exiting this access list.')
rsRuleStats = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6)).setObjects(("NOKIA-RATESHAPE-MIB", "rsRuleStatIfIndex"), ("NOKIA-RATESHAPE-MIB", "rsRuleStatIndex"), ("NOKIA-RATESHAPE-MIB", "rsRuleStatDirection"), ("NOKIA-RATESHAPE-MIB", "rsRuleStatDropPkts"), ("NOKIA-RATESHAPE-MIB", "rsRuleStatDropOctets"), ("NOKIA-RATESHAPE-MIB", "rsRuleStatPktsPassed"), ("NOKIA-RATESHAPE-MIB", "rsRuleStatBytesPassed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRuleStats = rsRuleStats.setStatus('current')
if mibBuilder.loadTexts: rsRuleStats.setDescription('A collection of objects providing the instrumentation of rsRuleStats')
rsRuleStatTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1), )
if mibBuilder.loadTexts: rsRuleStatTable.setStatus('current')
if mibBuilder.loadTexts: rsRuleStatTable.setDescription('A table of rate limit status entries.')
rsRuleStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1), ).setIndexNames((0, "NOKIA-RATESHAPE-MIB", "rsRuleStatIfIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsRuleStatIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsRuleStatDirection"))
if mibBuilder.loadTexts: rsRuleStatEntry.setStatus('current')
if mibBuilder.loadTexts: rsRuleStatEntry.setDescription('A collection of rate-limit status objects on this interface. ')
rsRuleStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatIfIndex.setStatus('current')
if mibBuilder.loadTexts: rsRuleStatIfIndex.setDescription('The value of ifIndex which corresponds to the interface for which this rule is applied to. ')
rsRuleStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatIndex.setStatus('current')
if mibBuilder.loadTexts: rsRuleStatIndex.setDescription('The rsRuleIndex value of the rule this entry describes. ')
rsRuleStatDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 3), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatDirection.setStatus('current')
if mibBuilder.loadTexts: rsRuleStatDirection.setDescription('The data source for this rule.')
rsRuleStatDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatDropPkts.setStatus('current')
if mibBuilder.loadTexts: rsRuleStatDropPkts.setDescription('The counter of packets which exceeded this rate limit.')
rsRuleStatDropOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatDropOctets.setStatus('current')
if mibBuilder.loadTexts: rsRuleStatDropOctets.setDescription('The counter of bytes which exceeded this rate limit.')
rsRuleStatPktsPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatPktsPassed.setStatus('current')
if mibBuilder.loadTexts: rsRuleStatPktsPassed.setDescription('Gives the count of number of packets successfully exiting this rule.')
rsRuleStatBytesPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatBytesPassed.setStatus('current')
if mibBuilder.loadTexts: rsRuleStatBytesPassed.setDescription('Gives the count of number of bytes successfully exiting this rule.')
rsAggregationClassStats = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5)).setObjects(("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatIfIndex"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatIndex"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatDirection"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatShapedPkts"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatShapedOctets"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatEnqueuedPkts"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatEnqueuedOctets"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatDroppedPkts"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatDroppedOctets"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatInputPktsPassed"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatOutputPktsPassed"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatInputBytesPassed"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatOutputBytesPassed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsAggregationClassStats = rsAggregationClassStats.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStats.setDescription('A collection of objects providing the instrumentation of rsAggregationClassStats')
rsAggregationClassStatTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1), )
if mibBuilder.loadTexts: rsAggregationClassStatTable.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatTable.setDescription('A table of aggregation class status entries.')
rsAggregationClassStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1), ).setIndexNames((0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassStatIfIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassStatIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassStatDirection"))
if mibBuilder.loadTexts: rsAggregationClassStatEntry.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatEntry.setDescription('A collection of aggregation class status objects on this interface. Entries are created and deleted via the rate-limit command line interface.')
rsAggregationClassStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatIfIndex.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatIfIndex.setDescription('The value of ifIndex which corresponds to the interface for which this aggregation class handles tokens for.')
rsAggregationClassStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatIndex.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatIndex.setDescription('The value of rsAggregationClassIndex for the aggregation class which this entry describes. ')
rsAggregationClassStatDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 3), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatDirection.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatDirection.setDescription('The data source for this aggregation class.')
rsAggregationClassStatShapedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatShapedPkts.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatShapedPkts.setDescription('The counter of packets shaped by this rate limit.')
rsAggregationClassStatShapedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatShapedOctets.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatShapedOctets.setDescription('The counter of bytes shaped by this interface.')
rsAggregationClassStatEnqueuedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatEnqueuedPkts.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatEnqueuedPkts.setDescription('The counter of packets enqueued by this rate limit.')
rsAggregationClassStatEnqueuedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatEnqueuedOctets.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatEnqueuedOctets.setDescription('The counter of enqueued bytes by this rate limit.')
rsAggregationClassStatDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatDroppedPkts.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatDroppedPkts.setDescription('The counter of packets which exceeded this rate limit.')
rsAggregationClassStatDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatDroppedOctets.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatDroppedOctets.setDescription('The counter of bytes which exceeded this rate limit.')
rsAggregationClassStatInputPktsPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatInputPktsPassed.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatInputPktsPassed.setDescription('The counter of packets successfully exiting this aggregation class.')
rsAggregationClassStatOutputPktsPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatOutputPktsPassed.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatOutputPktsPassed.setDescription('The counter of packets successfully exiting this aggregation class.')
rsAggregationClassStatInputBytesPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatInputBytesPassed.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatInputBytesPassed.setDescription('The counter of bytes successfully exiting this aggregation class.')
rsAggregationClassStatOutputBytesPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatOutputBytesPassed.setStatus('current')
if mibBuilder.loadTexts: rsAggregationClassStatOutputBytesPassed.setDescription('The counter of bytes successfully exiting this aggregation class.')
mibBuilder.exportSymbols("NOKIA-RATESHAPE-MIB", RateLimitAction=RateLimitAction, PacketSource=PacketSource, ntcRS=ntcRS, rsRuleStatDirection=rsRuleStatDirection, rsRuleAggregationClassIndex=rsRuleAggregationClassIndex, rsRuleStats=rsRuleStats, rsRuleStatIfIndex=rsRuleStatIfIndex, rsAccessListStatBytesPassed=rsAccessListStatBytesPassed, ntcCommon=ntcCommon, rsRuleTOS=rsRuleTOS, rsAggregationClassStatIndex=rsAggregationClassStatIndex, rsAccessListName=rsAccessListName, rsAccessListRowStatus=rsAccessListRowStatus, rsAccessListStatIfIndex=rsAccessListStatIfIndex, rsRuleDirection=rsRuleDirection, rsAggregationClassDirection=rsAggregationClassDirection, rsAccessListIfIndex=rsAccessListIfIndex, rsAggregationClassIfIndex=rsAggregationClassIfIndex, rsRuleDestAddress=rsRuleDestAddress, rsRuleIndex=rsRuleIndex, rsAccessListDirection=rsAccessListDirection, rsAccessListStatDirection=rsAccessListStatDirection, rsRuleSrcAddrMask=rsRuleSrcAddrMask, rsRuleDestStartingPort=rsRuleDestStartingPort, rsAggregationClassStatEnqueuedOctets=rsAggregationClassStatEnqueuedOctets, rsAggregationClassStats=rsAggregationClassStats, rsAggregationClassStatInputPktsPassed=rsAggregationClassStatInputPktsPassed, rsAggregationClassStatOutputPktsPassed=rsAggregationClassStatOutputPktsPassed, rsRuleDestEndingPort=rsRuleDestEndingPort, rsAccessListStatPktsPassed=rsAccessListStatPktsPassed, rsRuleDestAddrMask=rsRuleDestAddrMask, rsAggregationClassMeanRate=rsAggregationClassMeanRate, rsAggregationClassIndex=rsAggregationClassIndex, rsAccessListStatEntry=rsAccessListStatEntry, rsRuleSrcStartingPort=rsRuleSrcStartingPort, rsRuleStatDropOctets=rsRuleStatDropOctets, rsAggregationClassStatEnqueuedPkts=rsAggregationClassStatEnqueuedPkts, rsAggregationClassStatEntry=rsAggregationClassStatEntry, rsAccessListTable=rsAccessListTable, nokia=nokia, rsAggregationClassName=rsAggregationClassName, rsRuleIfIndex=rsRuleIfIndex, rsRuleSrcEndingPort=rsRuleSrcEndingPort, rsAggregationClassStatInputBytesPassed=rsAggregationClassStatInputBytesPassed, rsAccessListStatTable=rsAccessListStatTable, rsRuleStatEntry=rsRuleStatEntry, rsAggregationClassStatIfIndex=rsAggregationClassStatIfIndex, rsRuleEntry=rsRuleEntry, rsRuleStatTable=rsRuleStatTable, rsAccessListEntry=rsAccessListEntry, nokiaProducts=nokiaProducts, rsAggregationClassStatOutputBytesPassed=rsAggregationClassStatOutputBytesPassed, rsRuleStatPktsPassed=rsRuleStatPktsPassed, rsAccessListIndex=rsAccessListIndex, rsAggregationClasses=rsAggregationClasses, rsAccessListStatIndex=rsAccessListStatIndex, PYSNMP_MODULE_ID=ntcRS, rsRules=rsRules, rsRuleRowStatus=rsRuleRowStatus, rsAggregationClassStatShapedOctets=rsAggregationClassStatShapedOctets, rsRuleTable=rsRuleTable, rsRuleStatBytesPassed=rsRuleStatBytesPassed, rsAccessLists=rsAccessLists, rsRuleAction=rsRuleAction, rsRuleEstablished=rsRuleEstablished, rsRuleIpProtocol=rsRuleIpProtocol, rsAggregationClassTable=rsAggregationClassTable, rsAggregationClassEntry=rsAggregationClassEntry, rsAggregationClassStatDroppedPkts=rsAggregationClassStatDroppedPkts, rsAggregationClassRowStatus=rsAggregationClassRowStatus, rsAggregationClassStatTable=rsAggregationClassStatTable, rsAggregationClassStatShapedPkts=rsAggregationClassStatShapedPkts, rsRuleSrcAddress=rsRuleSrcAddress, rsAggregationClassStatDirection=rsAggregationClassStatDirection, rsAggregationClassBurstSize=rsAggregationClassBurstSize, rsAccessListStats=rsAccessListStats, rsRuleStatIndex=rsRuleStatIndex, rsAggregationClassStatDroppedOctets=rsAggregationClassStatDroppedOctets, rsRuleStatDropPkts=rsRuleStatDropPkts)
