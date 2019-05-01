#
# PySNMP MIB module CISCO-FLOW-MONITOR-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FLOW-MONITOR-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:58:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, MibIdentifier, NotificationType, ObjectIdentity, ModuleIdentity, Counter32, iso, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "MibIdentifier", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Counter32", "iso", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFlowMonitorTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 688))
ciscoFlowMonitorTcMIB.setRevisions(('2008-12-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFlowMonitorTcMIB.setRevisionsDescriptions(('The initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoFlowMonitorTcMIB.setLastUpdated('200812090000Z')
if mibBuilder.loadTexts: ciscoFlowMonitorTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFlowMonitorTcMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoFlowMonitorTcMIB.setDescription("This MIB module defines textual conventions used by the MIB modules defining objects describing flow monitoring. GLOSSARY ============ Alarm Action - a method used by the device to signal changes in an alarm condition. Alarm Aggregation - a technique used to efficiently monitor the same standing condition for a flow set. Alarm Condition - a standing condition for which the device signals changes in state. Alarm Group - a flow set for which the device monitors a configured standing condition, raising an alarm when a configured number of flows in the flow set assert the standing standing. Alarm Severity - the relative disposition of an alarm condition when raised by the device. For example, a provider may regard a flow stop alarm as having a higher severity than a flow's loss fraction exceeding a configured threshold. Flow Monitor - a hardware or software entity that classifies traffic flows, collects flow data, and periodically computes flow metrics. Flow Metric - a measurement that reflects the quality of a traffic flow. Flow Point - represents the ingress or egress of a traffic flow. Flow Set - a group of traffic flows. Measurement Interval - the length of time over which a flow monitor collects data related to a traffic flow, after which the flow monitor computes flow metrics using the collected data. Standing Condition - represents a lasting error, fault, or warning resulting from the application of a set of criteria to the state of an entity, such as a flow monitor or traffic flow. For example, a flow monitor may assert a standing condition if the number of traffic flows that expire in a meansurement interval exceeds a configured threshold. Traffic Flow - a unidirectional stream of packets conforming to a classifier. For example, packets having a particular source IP address, destination IP address, protocol type, source port number, and destination port number. ")
class FlowMonitorIdentifier(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an arbitrary integer-value that uniquely identifies a flow monitor.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FlowIdentifier(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an arbitrary integer-value that uniquely identifies a traffic flow within the scope of the flow monitor that collects data and periodically computes metrics for the traffic flow.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FlowPointType(TextualConvention, Integer32):
    reference = "K. McCloghrie and F. Kastenholz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    description = "This textual convention denotes an enumerated integer-value that represents a point at which a flow monitor collects data for a traffic flow: 'other' The implementation of the MIB module using this textual convention does not recognize the flow point. 'unknown' The device is unable to ascertain the point at which the flow monitor collects data for the traffic flow. 'none' There is no point at which the flow monitor collects data for the traffic flow. 'interface' The flow point is an interface represented by a row in the ifTable (defined by the IF-MIB [RFC2863]. 'dot1qVlan' The flow point is an IEEE 802.1q VLAN represented by a row in the ifTable (defined by the IF-MIB [RFC2863]) and a tag representing the VLAN. With the exception of the values 'unknown' and 'none', each definition of a concrete FlowPointType value MUST have a corresponding textual convention for use with the particular type of flow point. To support future extensions, a MIB module SHOULD NOT sub-type the FlowPointType textual convention in an object type definition. However, a compliance statement MAY sub-type it in order to require only a subset of the flow point types for a compliant implementation. Implementations must ensure that FlowPointType objects and any dependent objects (e.g., FlowPointIdentifier objects) are consistent. For example, an implementation must respond with an 'inconsistentValue' error if an attempt is made to modify a FlowPointType object without changing the corresponding FlowPointIdentifier object."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("none", 3), ("interface", 4), ("dot1qVlan", 5))

class FlowPointIdentifier(TextualConvention, OctetString):
    description = "This textual convention denotes an octet string-value that identifies a point at which a flow monitor collects data for a traffic flow. An implementation MUST ALWAYS interpret a FlowPointIdentifier value within the context of a FlowPointType value. Every use of the FlowPointIdentifier textual convention requires the specification of a FlowPointType object to provide the context. A MIB module SHOULD logically register the FlowPointType object before the FlowPointIdentifier object(s). The value of a FlowPointIdentifier object MUST BE the null string if the value of the FlowPointType object providing the context is 'unknown' or 'none'. Implementations must ensure that a FlowPointIdentifier object remains consistent with the FlowPointType object providing the context. For example, an implementation must respond with an 'inconsistentValue' error if an attempt is made to modify a FlowPointIdentifier object without changing the corresponding FlowPointType object."
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class FlowPointInterface(TextualConvention, OctetString):
    reference = "K. McCloghrie and F. Kastenholz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    description = "This textual convention denotes an octet string-value identifying a row in ifTable (defined by the IF-MIB [RFC2863]). Octets Contents Encoding ========================================= 1-4 ifIndex-value network-byte order The corresponding FlowPointType value is 'interface'. A MIB module SHOULD NOT directly use this textual convention in defining object, as it restricts flow points to specific type. However, if a MIB module does chose to directly use the textual convention, it MAY chose to do so without a FlowPointType object to define the context, since this textual convention implies the context."
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class FlowPointDot1qVlan(TextualConvention, OctetString):
    reference = "K. McCloghrie and F. Kastenholz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    description = "This textual convention denotes an octet string-value identifying an IEEE 802.1q VLAN. Octets Contents Encoding ========================================= 1-4 ifIndex-value network-byte order 5-6 VLAN tag network-byte order The corresponding FlowPointType value is 'dot1qVlan'. A MIB module SHOULD NOT directly use this textual convention in defining object, as it restricts flow points to specific type. However, if a MIB module does chose to directly use the textual convention, it MAY chose to do so without a FlowPointType object to define the context, since this textual convention implies the context."
    status = 'current'
    displayHint = '4d,2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class FlowMetrics(TextualConvention, Bits):
    reference = "H. Schulzrinne, S. Casner, R. Fredrick, and V. Jacobson, 'RTP: A Transport Protocol for Real-Time Applications', RFC-3550, July 2003. J. Welch and J. Clark, 'A Proposed Media Delivery Index (MDI)', RFC-4445, APril 2006."
    description = "This textual convention denotes an enumerated integer-value that represents a set of metrics: 'mdi' This set of metrics consists of the Media Delivery Index (MDI) [RFC4445] 'rtp' This set of metrics consists of data similar to that computed and sent by a RTP client in a RTCP receiver report [RFC3550]. 'ipCbr' This set of metrics complements MDI, measuring the notion of Media Rate Variation (MRV)."
    status = 'current'
    namedValues = NamedValues(("mdi", 0), ("rtp", 1), ("ipCbr", 2))

class FlowCfgRateType(TextualConvention, Integer32):
    reference = "J. Welch and J. Clark, 'A Proposed Media Delivery Index (MDI)', RFC-4445, APril 2006."
    description = "This textual convention denotes an enumerated integer-value that represents the media rate used by the flow monitor to compute the delay factor for a traffic flow: 'auto' The device automatically determines the media rate. 'ipPktRate' The device uses a configured media rate expressed as an IP packet rate. 'ipBitRate' The device uses a configured media rate expressed as an IP packet rate. 'mediaRate' The device uses a configured media rate expressed as a media bit rate. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("auto", 1), ("ipPktRate", 2), ("ipBitRate", 3), ("mediaRate", 4))

class FlowBitRateUnits(TextualConvention, Integer32):
    description = "This textual convention denotes an enumerated integer-value that represents the units used when presenting a bit rate value. 'bps' The device presents the rate of a traffic flow in bits per second (bps). 'kbps' The device presents the rate of a traffic flow in Kbps. 'mbps' The device presents the rate of a traffic flow in Mbps. 'gbps' The device presents the rate of a traffic flow in Gbps."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("bps", 1), ("kbps", 2), ("mbps", 3), ("gbps", 4))

class FlowMetricScale(TextualConvention, Integer32):
    description = "This textual convention denotes an enumerated integer-value that represents an International System of Units (SI) prefix used as a scaling factor for fixed-point values: Prefix Scale Factor ========================= 'yocto' 10E-24 'zepto' 10E-21 'atto' 10E-18 'femto' 10E-15 'pico' 10E-12 'nano' 10E-9 'micro' 10E-6 'milli' 10E-3 'units' 10E0 'kilo' 10E3 'mega' 10E6 'giga' 10E9 'tera' 10E12 'exa' 10E15 'peta' 10E18 'zetta' 10E21 'yotta' 10E24 A MIB module may abstract a fixed-point value by defining three objects together: 1) A FlowMetricScale object, which indicates the scale of the value. 2) A FlowMetricPrecision object, which indicates the precision of the value. In the case that the value has a fractional portion, this object indicates the number of digits comprising the fractional portion. 3) A FlowMetricValue object, which indicates the value before scaling."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class FlowMetricPrecision(TextualConvention, Integer32):
    description = "This textual convention denotes the precision or accuracy of a fixed-point value. A MIB module may abstract a fixed-point value by defining three objects together: 1) A FlowMetricScale object, which indicates the scale of the value. 2) A FlowMetricPrecision object, which indicates the precision of the value. In the case that the value has a fractional portion, this object indicates the number of digits comprising the fractional portion. 3) A FlowMetricValue object, which indicates the value before scaling. If an instance of an object of this type has a value in the range of 1 to 9, then it represents the precision of the associated value; that is, the number of decimal places in the fractional part of the associated value. For example, if the Media Loss Rate (MLR) computed for a traffic flow is 350.9E-6, then the FlowMetricScale object is 'micro', the FlowMetricPrecision object is 1, and the object indicating the value is 3509. If an instance of an object of this type has a value in the range of -8 to -1, then it represents the number of accurate digits in the associated value. For example, if the jitter measured for a traffic flow can range between -100,000 and 100,000 microseconds in 10 microsecond increments, with an accuracy of +/- 5 microseconds, the FlowMetricScale object is 'micro', the FlowMetricPrecision object is -2, and the object indicating the value has range of -100,000 to 100,000."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-8, -1), ValueRangeConstraint(1, 9), )
class FlowMetricValue(TextualConvention, Integer32):
    description = 'This textual convention denotes the value of a fixed-point value. A MIB module may abstract a fixed-point value by defining three objects together: 1) A FlowMetricScale object, which indicates the scale of the value. 2) A FlowMetricPrecision object, which indicates the precision of the value. In the case that the value has a fractional portion, this object indicates the number of digits comprising the fractional portion. 3) A FlowMetricValue object, which indicates the value before scaling.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class FlowMonitorConditions(TextualConvention, OctetString):
    description = 'This textual convention denotes a octet string-value that represents the standing conditions associated with an entity, such as a flow monitor a traffic flow. Each bit in the string corresponds to a single standing condition. The device should present a description of the standing condition in the cfmConditionTable, which uniquely identifies such a description by the following tuple: [cfmConditionProfile, cfmConditionId] where cfmConditionProfile uniquely identifies the conditions profile containing the description and cfmConditionId corresponds to the bit position within the string. The figure below illustrates a representation of the string containing N octets: Octet 0 Octet N-1 7 6 5 4 3 2 1 0 7 6 5 4 3 2 1 0 +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ | |...| | +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | +- Condition 8(n-1) | | | | | | | | | | | | | | +--- Condition 8(n-1)+1 | | | | | | | | | | | | | +----- Condition 8(n-1)+2 | | | | | | | | | | | | +------- Condition 8(n-1)+3 | | | | | | | | | | | +--------- Condition 8(n-1)+4 | | | | | | | | | | +----------- Condition 8(n-1)+5 | | | | | | | | | +------------- Condition 8(n-1)+6 | | | | | | | | +--------------- Condition 8(n-1)+7 | | | | | | | | : | | | | | | | | : | | | | | | | +--------------------- Condition 0 | | | | | | +----------------------- Condition 1 | | | | | +------------------------- Condition 2 | | | | +--------------------------- Condition 3 | | | +----------------------------- Condition 4 | | +------------------------------- Condition 5 | +--------------------------------- Condition 6 +----------------------------------- Condition 7'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class FlowMonitorConditionsProfile(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an arbitrary integer-value that uniquely identifies a conditions profile. A conditions profile is a set of descriptions of standing/alarm conditions that can be applied to an entity, such as a flow alarm or a traffic flow.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FlowMonitorConditionsProfileOrZero(TextualConvention, Unsigned32):
    description = "This textual convention serves as an extension of the FlowMonitorConditionsProfile textual convention, which permits the value '0'. The use of the value '0' is specific to an object, thus requiring the descriptive text associated with the object to describe the semantics of its use."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class FlowMonitorConditionIdentifier(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an integer-value representing a standing/alarm condition within a conditions profile. It has a direct correspondence to the position of the bit representing the standing/alarm condition in a FlowMonitorConditions object.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 2039)

class FlowMonitorAlarmGroupIdentifier(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an arbitrary integer-value that uniquely identifies an alarm group. An alarm group represents an alarm condition that the device raises if a configured number of traffic flows in a configured set of traffic flows asserts a given standing condition.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FlowSetIdentifier(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an arbitrary integer-value that uniquely identifies a set of traffic flows.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

mibBuilder.exportSymbols("CISCO-FLOW-MONITOR-TC-MIB", FlowIdentifier=FlowIdentifier, FlowMetrics=FlowMetrics, FlowPointInterface=FlowPointInterface, FlowMetricScale=FlowMetricScale, FlowBitRateUnits=FlowBitRateUnits, FlowMonitorConditionsProfile=FlowMonitorConditionsProfile, FlowMonitorConditions=FlowMonitorConditions, PYSNMP_MODULE_ID=ciscoFlowMonitorTcMIB, FlowMetricPrecision=FlowMetricPrecision, FlowPointType=FlowPointType, FlowSetIdentifier=FlowSetIdentifier, ciscoFlowMonitorTcMIB=ciscoFlowMonitorTcMIB, FlowCfgRateType=FlowCfgRateType, FlowPointDot1qVlan=FlowPointDot1qVlan, FlowMonitorIdentifier=FlowMonitorIdentifier, FlowMonitorAlarmGroupIdentifier=FlowMonitorAlarmGroupIdentifier, FlowPointIdentifier=FlowPointIdentifier, FlowMetricValue=FlowMetricValue, FlowMonitorConditionsProfileOrZero=FlowMonitorConditionsProfileOrZero, FlowMonitorConditionIdentifier=FlowMonitorConditionIdentifier)
