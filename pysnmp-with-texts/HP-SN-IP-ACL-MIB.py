#
# PySNMP MIB module HP-SN-IP-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-SN-IP-ACL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:36:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
snIp, = mibBuilder.importSymbols("HP-SN-ROOT-MIB", "snIp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, Counter64, Unsigned32, Bits, IpAddress, Gauge32, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter64", "Unsigned32", "Bits", "IpAddress", "Gauge32", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

class RtrStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class SnRowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4))

class Action(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("deny", 0), ("permit", 1))

class TruthVal(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("false", 0), ("true", 1))

class AclNumber(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 199)

class Operator(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 7))
    namedValues = NamedValues(("eq", 0), ("neq", 1), ("lt", 2), ("gt", 3), ("range", 4), ("undefined", 7))

class IpProtocol(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class PrecedenceValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(5, 3, 4, 2, 6, 7, 1, 0, 8))
    namedValues = NamedValues(("critical", 5), ("flash", 3), ("flashoverride", 4), ("immediate", 2), ("internet", 6), ("network", 7), ("priority", 1), ("routine", 0), ("undefined", 8))

class TosValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("normal", 0), ("minMonetaryCost", 1), ("maxReliability", 2), ("tosValue3", 3), ("maxThroughput", 4), ("tosValue5", 5), ("tosValue6", 6), ("tosValue7", 7), ("minDelay", 8), ("tosValue9", 9), ("tosValue10", 10), ("tosValue11", 11), ("tosValue12", 12), ("tosValue13", 13), ("tosValue14", 14), ("tosValue15", 15), ("undefined", 16))

class Direction(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("inbound", 0), ("outbound", 1))

snAgAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15))
snAgAclGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 1))
snAgAclGblCurRowIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclGblCurRowIndex.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclGblCurRowIndex.setDescription('The current row index of the ACL table entry.')
snAgAclTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2), )
if mibBuilder.loadTexts: snAgAclTable.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclTable.setDescription('Table of Access Control List')
snAgAclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1), ).setIndexNames((0, "HP-SN-IP-ACL-MIB", "snAgAclIndex"))
if mibBuilder.loadTexts: snAgAclEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclEntry.setDescription('An entry in the IP access control list table.')
snAgAclIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclIndex.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclIndex.setDescription('The access control list item number for an entry. This is a unique number that identifies different Access list entries combined with the access list name and access list number. This one has to be unique even though the name and number are not unique for a give access list with same or different source address, subnet mask, destination address and destination mask, protocol type, action (permit/deny) type and the operator (neq, eq, gt and , lt) which makes the index a unique tuple (name, number, itemnumber).')
snAgAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 2), AclNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclNumber.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclNumber.setDescription('The access control list number for an entry. The standard access list is in the range <1..99>. The extended access list is in the range <100-199>.')
snAgAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclName.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclName.setDescription('ACL name for an entry.')
snAgAclAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 4), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclAction.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclAction.setDescription('Action to take if the ip packet matches with this access control list.')
snAgAclProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 5), IpProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclProtocol.setDescription('Transport protocol. 0 means any protocol.')
snAgAclSourceIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceIp.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclSourceIp.setDescription('Source IP address.')
snAgAclSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceMask.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclSourceMask.setDescription('Source IP subnet mask.')
snAgAclSourceOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 8), Operator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceOperator.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclSourceOperator.setDescription('Type of comparison to perform. for now, this only applys to tcp or udp to compare the port number')
snAgAclSourceOperand1 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceOperand1.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclSourceOperand1.setDescription('For now this only refers to transport protocol port number. 0 means NA')
snAgAclSourceOperand2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclSourceOperand2.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclSourceOperand2.setDescription('For now this only refers to transport protocol port number. 0 means NA')
snAgAclDestinationIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationIp.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclDestinationIp.setDescription('Destination IP address.')
snAgAclDestinationMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationMask.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclDestinationMask.setDescription('Destination IP subnet mask.')
snAgAclDestinationOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 13), Operator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationOperator.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclDestinationOperator.setDescription('Type of comparison to perform. for now, this only applys to tcp or udp to compare the port number')
snAgAclDestinationOperand1 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationOperand1.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclDestinationOperand1.setDescription('For now this only refers to transport protocol port number. 0 means NA')
snAgAclDestinationOperand2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDestinationOperand2.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclDestinationOperand2.setDescription('For now this only refers to transport protocol port number. 0 means NA')
snAgAclPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 16), PrecedenceValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclPrecedence.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclPrecedence.setDescription('This refers to IP precedence value in the range <0-7> critical(5), flash(3), flash-override(4), immediate(2), internet(6), network(7), priority(1), routine(0)')
snAgAclTos = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 17), TosValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclTos.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclTos.setDescription('This refers to the IP type of service value in range <0-15> which is the sum of numeric vlaues of the following options - match packets with maximum reliability TOS (2) match packets with maximum throughput TOS (4) match packets with minimum delay (8) match packets with minimum monetary cost TOS (1) match packets with normal TOS (0)')
snAgAclEstablished = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 18), RtrStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclEstablished.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclEstablished.setDescription('Enable/Disable the filtering of established TCP packets of which the ACK or RESET flag is on. This additional filter only applies to TCP transport protocol.')
snAgAclLogOption = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 19), TruthVal()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclLogOption.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclLogOption.setDescription('Log flag')
snAgAclStandardFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 20), TruthVal()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclStandardFlag.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclStandardFlag.setDescription('Return whether the ACL is standard or extended, 1 for standard ACL')
snAgAclRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 21), SnRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclRowStatus.setDescription('To create or delete a access list entry.')
snAgAclFlowCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclFlowCounter.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclFlowCounter.setDescription('Approximate count of flows matching individual ACL entry.')
snAgAclPacketCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclPacketCounter.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclPacketCounter.setDescription('Accurate count of packets matching individual ACL entry.')
snAgAclComments = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 24), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclComments.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclComments.setDescription('Remark description of individual ACL entry.')
snAgAclIpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclIpPriority.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclIpPriority.setDescription('QoS priority option for IP ACL entry.')
snAgAclPriorityForce = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclPriorityForce.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclPriorityForce.setDescription('Force packet outgoing priority. Not defined(4)')
snAgAclPriorityMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclPriorityMapping.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclPriorityMapping.setDescription('Map incoming packet priority. Not defined(8)')
snAgAclDscpMarking = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDscpMarking.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclDscpMarking.setDescription('Mark packets with given DSCP value. Not defined(64)')
snAgAclDscpMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclDscpMapping.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclDscpMapping.setDescription('Map incoming DSCP value. Not defined(64)')
snAgAclBindToPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3), )
if mibBuilder.loadTexts: snAgAclBindToPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclBindToPortTable.setDescription('Table of ACL binding to port for router')
snAgAclBindToPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1), ).setIndexNames((0, "HP-SN-IP-ACL-MIB", "snAgAclPortNum"), (0, "HP-SN-IP-ACL-MIB", "snAgAclPortBindDirection"))
if mibBuilder.loadTexts: snAgAclBindToPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclBindToPortEntry.setDescription('An entry in the ACL-binding-to-port table.')
snAgAclPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclPortNum.setDescription('Binding-to port num, either physical port or virtual interface.')
snAgAclPortBindDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 2), Direction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgAclPortBindDirection.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclPortBindDirection.setDescription('ACL port direction, inbound or outbound')
snAgAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclNum.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclNum.setDescription('Defined ACL number')
snAgAclNameString = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclNameString.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclNameString.setDescription('Defined ACL name')
snAgBindPortListInVirtualInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgBindPortListInVirtualInterface.setStatus('mandatory')
if mibBuilder.loadTexts: snAgBindPortListInVirtualInterface.setDescription('Port list for binding virtual interface')
snAgAclPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 6), SnRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snAgAclPortRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: snAgAclPortRowStatus.setDescription('To create or delete a ACL port entry.')
mibBuilder.exportSymbols("HP-SN-IP-ACL-MIB", snAgAclPriorityForce=snAgAclPriorityForce, RtrStatus=RtrStatus, snAgAclTable=snAgAclTable, snAgAclDscpMapping=snAgAclDscpMapping, snAgAclBindToPortTable=snAgAclBindToPortTable, DisplayString=DisplayString, snAgAclName=snAgAclName, Operator=Operator, snAgAclEntry=snAgAclEntry, snAgAclAction=snAgAclAction, snAgAclEstablished=snAgAclEstablished, PrecedenceValue=PrecedenceValue, snAgAclNum=snAgAclNum, snAgAclPortRowStatus=snAgAclPortRowStatus, snAgAclPrecedence=snAgAclPrecedence, snAgAclPacketCounter=snAgAclPacketCounter, snAgAclDscpMarking=snAgAclDscpMarking, IpProtocol=IpProtocol, snAgAclIpPriority=snAgAclIpPriority, TruthVal=TruthVal, snAgAclLogOption=snAgAclLogOption, AclNumber=AclNumber, Direction=Direction, snAgAclSourceOperand1=snAgAclSourceOperand1, SnRowStatus=SnRowStatus, snAgAclDestinationOperand2=snAgAclDestinationOperand2, snAgAclSourceIp=snAgAclSourceIp, snAgAclStandardFlag=snAgAclStandardFlag, snAgAclProtocol=snAgAclProtocol, snAgAclPortNum=snAgAclPortNum, snAgAclDestinationOperand1=snAgAclDestinationOperand1, snAgAclSourceOperand2=snAgAclSourceOperand2, snAgAcl=snAgAcl, Action=Action, snAgAclDestinationOperator=snAgAclDestinationOperator, snAgAclPriorityMapping=snAgAclPriorityMapping, snAgAclComments=snAgAclComments, snAgAclNumber=snAgAclNumber, snAgAclGlobal=snAgAclGlobal, snAgAclTos=snAgAclTos, snAgAclSourceMask=snAgAclSourceMask, snAgAclSourceOperator=snAgAclSourceOperator, snAgAclRowStatus=snAgAclRowStatus, snAgAclFlowCounter=snAgAclFlowCounter, snAgAclDestinationIp=snAgAclDestinationIp, snAgBindPortListInVirtualInterface=snAgBindPortListInVirtualInterface, snAgAclBindToPortEntry=snAgAclBindToPortEntry, snAgAclIndex=snAgAclIndex, snAgAclDestinationMask=snAgAclDestinationMask, snAgAclGblCurRowIndex=snAgAclGblCurRowIndex, snAgAclNameString=snAgAclNameString, snAgAclPortBindDirection=snAgAclPortBindDirection, TosValue=TosValue)