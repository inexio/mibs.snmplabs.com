#
# PySNMP MIB module APERTUS-UA-FALLBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APERTUS-UA-FALLBACK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:23:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, Gauge32, Counter64, NotificationType, IpAddress, MibIdentifier, Unsigned32, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Gauge32", "Counter64", "NotificationType", "IpAddress", "MibIdentifier", "Unsigned32", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "ObjectIdentity", "Bits", "Counter32")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
internet = MibIdentifier((1, 3, 6, 1))
directory = MibIdentifier((1, 3, 6, 1, 1))
mgmt = MibIdentifier((1, 3, 6, 1, 2))
experimental = MibIdentifier((1, 3, 6, 1, 3))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
apertus = MibIdentifier((1, 3, 6, 1, 4, 1, 543))
isg = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3))
aperua = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3))
aperfallback = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 3))
aperFallbackMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1))
aperFallbackMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1))
aperFallbackConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 1))
aperFallbackDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2))
aperFallbackNode = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3))
aperFallbackConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ready", 1), ("loading", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackConfigStatus.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackConfigStatus.setDescription('Status of Universal Access server')
aperFallbackConfigUpTime = MibScalar((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackConfigUpTime.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackConfigUpTime.setDescription('This value represents the time elapsed since the server was started in 1/100nths of a second.')
aperFallbackDomainTable = MibTable((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1), )
if mibBuilder.loadTexts: aperFallbackDomainTable.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackDomainTable.setDescription('Domain information broken down domain name.')
aperFallbackDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1, 1), ).setIndexNames((0, "APERTUS-UA-FALLBACK-MIB", "aperFallbackDomainName"))
if mibBuilder.loadTexts: aperFallbackDomainEntry.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackDomainEntry.setDescription('This table contains information on each of the load balance domains under its control.')
aperFallbackDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackDomainName.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackDomainName.setDescription('The zone name for this load-balance domain.')
aperFallbackDomainUpServers = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackDomainUpServers.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackDomainUpServers.setDescription('The number of servers that are up at this time.')
aperFallbackDomainDownServers = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackDomainDownServers.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackDomainDownServers.setDescription('The number of servers in list that are marked as down at this time.')
aperFallbackNodeTable = MibTable((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1), )
if mibBuilder.loadTexts: aperFallbackNodeTable.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackNodeTable.setDescription('Node information broken down domain name and IP address')
aperFallbackNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1), ).setIndexNames((0, "APERTUS-UA-FALLBACK-MIB", "aperFallbackNodeName"), (0, "APERTUS-UA-FALLBACK-MIB", "aperFallbackNodeIP"))
if mibBuilder.loadTexts: aperFallbackNodeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackNodeEntry.setDescription('This table contains information on each of the machines in the different laod balance zones.')
aperFallbackNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackNodeName.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackNodeName.setDescription('The zone name for this Node.')
aperFallbackNodeIP = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackNodeIP.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackNodeIP.setDescription('The IP address of the NODE.')
aperFallbackNodeHostIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackNodeHostIndex.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackNodeHostIndex.setDescription('This value is the host index within the domain. The lower the number, the higher the preference towards using the node for all name to address mappings.')
aperFallbackNodePoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackNodePoolIndex.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackNodePoolIndex.setDescription('This value is the pool index. When all nodes with a lower index are down, the items with next highest pool index are considered for fallback usage.')
aperFallbackNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("notqueried", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackNodeStatus.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackNodeStatus.setDescription('Indicates the status of the node. Up(1) shows that the node is up and is being considered for use. Down(2) indicates that the last query to the NODE image resulted in a down marker for the node. Admindown(3) indicates that an administrator took the node offline manually (from the UA server end). Notqueried(4) is used to indicate that a node has never been queried.')
aperFallbackNodeResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackNodeResponseTime.setStatus('mandatory')
if mibBuilder.loadTexts: aperFallbackNodeResponseTime.setDescription('Response time in MS of last node access. A value of 0 is returned if NodeStatus is not ready(1) or if the node has never been queried')
mibBuilder.exportSymbols("APERTUS-UA-FALLBACK-MIB", private=private, aperFallbackNodePoolIndex=aperFallbackNodePoolIndex, internet=internet, enterprises=enterprises, aperfallback=aperfallback, aperFallbackDomainTable=aperFallbackDomainTable, isg=isg, apertus=apertus, aperFallbackNodeEntry=aperFallbackNodeEntry, aperFallbackDomainUpServers=aperFallbackDomainUpServers, aperFallbackNodeName=aperFallbackNodeName, aperua=aperua, aperFallbackNodeTable=aperFallbackNodeTable, aperFallbackMIB=aperFallbackMIB, aperFallbackConfigUpTime=aperFallbackConfigUpTime, aperFallbackNodeResponseTime=aperFallbackNodeResponseTime, aperFallbackDomainName=aperFallbackDomainName, aperFallbackNodeHostIndex=aperFallbackNodeHostIndex, aperFallbackDomainEntry=aperFallbackDomainEntry, mgmt=mgmt, aperFallbackConfig=aperFallbackConfig, aperFallbackNode=aperFallbackNode, aperFallbackDomainDownServers=aperFallbackDomainDownServers, aperFallbackMIBObjects=aperFallbackMIBObjects, aperFallbackNodeIP=aperFallbackNodeIP, aperFallbackDomain=aperFallbackDomain, experimental=experimental, directory=directory, aperFallbackNodeStatus=aperFallbackNodeStatus, aperFallbackConfigStatus=aperFallbackConfigStatus)
