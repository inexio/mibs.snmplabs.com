#
# PySNMP MIB module FSM7326-QOS-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FSM7326-QOS-ACL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:16:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
fsm7326QOS, = mibBuilder.importSymbols("FSM7326-QOS-MIB", "fsm7326QOS")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Integer32, MibIdentifier, Bits, Counter64, ObjectIdentity, iso, NotificationType, TimeTicks, Unsigned32, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Integer32", "MibIdentifier", "Bits", "Counter64", "ObjectIdentity", "iso", "NotificationType", "TimeTicks", "Unsigned32", "Counter32", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
fsm7326QOSACL = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2))
fsm7326QOSACL.setRevisions(('2003-11-10 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fsm7326QOSACL.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: fsm7326QOSACL.setLastUpdated('200311101200Z')
if mibBuilder.loadTexts: fsm7326QOSACL.setOrganization('Netgear')
if mibBuilder.loadTexts: fsm7326QOSACL.setContactInfo('')
if mibBuilder.loadTexts: fsm7326QOSACL.setDescription('')
aclTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 1), )
if mibBuilder.loadTexts: aclTable.setStatus('current')
if mibBuilder.loadTexts: aclTable.setDescription('A table of ACL instances.')
aclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 1, 1), ).setIndexNames((0, "FSM7326-QOS-ACL-MIB", "aclIndex"))
if mibBuilder.loadTexts: aclEntry.setStatus('current')
if mibBuilder.loadTexts: aclEntry.setDescription('')
aclStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclStatus.setStatus('current')
if mibBuilder.loadTexts: aclStatus.setDescription('Status of this instance. active(1) - this ACL instance is active createAndGo(4) - set to this value to create an instance destroy(6) - set to this value to delete an instance')
aclIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: aclIndex.setStatus('current')
if mibBuilder.loadTexts: aclIndex.setDescription('The ACL index this instance is associated with.')
aclIfTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 2), )
if mibBuilder.loadTexts: aclIfTable.setStatus('current')
if mibBuilder.loadTexts: aclIfTable.setDescription('A table of ACL interface instances.')
aclIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 2, 1), ).setIndexNames((0, "FSM7326-QOS-ACL-MIB", "aclIndex"), (0, "FSM7326-QOS-ACL-MIB", "aclIfIndex"), (0, "FSM7326-QOS-ACL-MIB", "aclIfDirection"))
if mibBuilder.loadTexts: aclIfEntry.setStatus('current')
if mibBuilder.loadTexts: aclIfEntry.setDescription('')
aclIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: aclIfIndex.setStatus('current')
if mibBuilder.loadTexts: aclIfIndex.setDescription('The interface this ACL instance is associated with.')
aclIfDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2))))
if mibBuilder.loadTexts: aclIfDirection.setStatus('current')
if mibBuilder.loadTexts: aclIfDirection.setDescription('The direction this ACL instance applies.')
aclIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclIfStatus.setStatus('current')
if mibBuilder.loadTexts: aclIfStatus.setDescription('Status of this instance. active(1) - this ACL index instance is active createAndGo(4) - set to this value to assign an interface to an ACL destroy(6) - set to this value to remove an interface to an ACL')
aclRuleTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3), )
if mibBuilder.loadTexts: aclRuleTable.setStatus('current')
if mibBuilder.loadTexts: aclRuleTable.setDescription('A table of ACL Rules instances.')
aclRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1), ).setIndexNames((0, "FSM7326-QOS-ACL-MIB", "aclIndex"), (0, "FSM7326-QOS-ACL-MIB", "aclRuleIndex"))
if mibBuilder.loadTexts: aclRuleEntry.setStatus('current')
if mibBuilder.loadTexts: aclRuleEntry.setDescription('A table of ACL Classification Rules')
aclRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: aclRuleIndex.setStatus('current')
if mibBuilder.loadTexts: aclRuleIndex.setDescription('The index of this instance.')
aclRuleAction = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2))).clone('deny')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleAction.setStatus('current')
if mibBuilder.loadTexts: aclRuleAction.setDescription('The type of action this rule should perform.')
aclRuleProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleProtocol.setStatus('current')
if mibBuilder.loadTexts: aclRuleProtocol.setDescription('icmp - 1 igmp - 2 ip - 4 tcp - 6 udp - 17 All values from 1 to 255 are valid.')
aclRuleSrcIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleSrcIpAddress.setStatus('current')
if mibBuilder.loadTexts: aclRuleSrcIpAddress.setDescription('The Source IP Address used in the ACL Classification.')
aclRuleSrcIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleSrcIpMask.setStatus('current')
if mibBuilder.loadTexts: aclRuleSrcIpMask.setDescription('The Source IP Mask used in the ACL Classification.')
aclRuleSrcL4Port = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleSrcL4Port.setStatus('current')
if mibBuilder.loadTexts: aclRuleSrcL4Port.setDescription('The Source Port Number (Layer 4) used in the ACL Classification.')
aclRuleSrcL4PortRangeStart = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleSrcL4PortRangeStart.setStatus('current')
if mibBuilder.loadTexts: aclRuleSrcL4PortRangeStart.setDescription('The Source Port Number(Layer 4) range start.')
aclRuleSrcL4PortRangeEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleSrcL4PortRangeEnd.setStatus('current')
if mibBuilder.loadTexts: aclRuleSrcL4PortRangeEnd.setDescription('The Source Port Number(Layer 4) range end.')
aclRuleDestIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleDestIpAddress.setStatus('current')
if mibBuilder.loadTexts: aclRuleDestIpAddress.setDescription('The Destination IP Address used in the ACL Classification.')
aclRuleDestIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleDestIpMask.setStatus('current')
if mibBuilder.loadTexts: aclRuleDestIpMask.setDescription('The Destination IP Mask used in the ACL Classification.')
aclRuleDestL4Port = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleDestL4Port.setStatus('current')
if mibBuilder.loadTexts: aclRuleDestL4Port.setDescription('The Destination Port (Layer 4) used in ACl classification.')
aclRuleDestL4PortRangeStart = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleDestL4PortRangeStart.setStatus('current')
if mibBuilder.loadTexts: aclRuleDestL4PortRangeStart.setDescription('The Destination Port (Layer 4) starting range used in ACL classification.')
aclRuleDestL4PortRangeEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleDestL4PortRangeEnd.setStatus('current')
if mibBuilder.loadTexts: aclRuleDestL4PortRangeEnd.setDescription('The Destination Port (Layer 4) ending range used in ACL classification.')
aclRuleIPDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 14), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleIPDSCP.setStatus('current')
if mibBuilder.loadTexts: aclRuleIPDSCP.setDescription('The Differentiated Services Code Point value.')
aclRuleIpPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleIpPrecedence.setStatus('current')
if mibBuilder.loadTexts: aclRuleIpPrecedence.setDescription('The Type of Service (TOS) IP Precedence value.')
aclRuleIpTosBits = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 16), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleIpTosBits.setStatus('current')
if mibBuilder.loadTexts: aclRuleIpTosBits.setDescription('The Type of Service (TOS) Bits value.')
aclRuleIpTosMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleIpTosMask.setStatus('current')
if mibBuilder.loadTexts: aclRuleIpTosMask.setDescription('The Type of Service (TOS) Mask value.')
aclRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclRuleStatus.setStatus('current')
if mibBuilder.loadTexts: aclRuleStatus.setDescription('Status of this instance. active(1) - this ACL Rule is active createAndGo(4) - set to this value to create an instance destroy(6) - set to this value to delete an instance')
mibBuilder.exportSymbols("FSM7326-QOS-ACL-MIB", aclRuleSrcIpAddress=aclRuleSrcIpAddress, aclRuleDestL4Port=aclRuleDestL4Port, aclIfDirection=aclIfDirection, aclIfEntry=aclIfEntry, PYSNMP_MODULE_ID=fsm7326QOSACL, aclRuleTable=aclRuleTable, aclRuleProtocol=aclRuleProtocol, aclRuleAction=aclRuleAction, aclIfStatus=aclIfStatus, aclRuleDestIpMask=aclRuleDestIpMask, aclRuleDestL4PortRangeEnd=aclRuleDestL4PortRangeEnd, aclRuleDestIpAddress=aclRuleDestIpAddress, aclRuleSrcL4Port=aclRuleSrcL4Port, aclRuleDestL4PortRangeStart=aclRuleDestL4PortRangeStart, aclRuleIpTosBits=aclRuleIpTosBits, aclStatus=aclStatus, aclRuleSrcIpMask=aclRuleSrcIpMask, aclRuleIPDSCP=aclRuleIPDSCP, aclRuleStatus=aclRuleStatus, aclRuleSrcL4PortRangeEnd=aclRuleSrcL4PortRangeEnd, aclRuleIpPrecedence=aclRuleIpPrecedence, aclRuleIpTosMask=aclRuleIpTosMask, aclRuleIndex=aclRuleIndex, aclTable=aclTable, aclIfTable=aclIfTable, aclEntry=aclEntry, aclRuleSrcL4PortRangeStart=aclRuleSrcL4PortRangeStart, aclRuleEntry=aclRuleEntry, aclIfIndex=aclIfIndex, aclIndex=aclIndex, fsm7326QOSACL=fsm7326QOSACL)
