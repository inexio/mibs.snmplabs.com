#
# PySNMP MIB module JUNIPER-L2CP-FEATURES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-L2CP-FEATURES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:59:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
dot1dStpPortEntry, dot1dStpPort = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStpPortEntry", "dot1dStpPort")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
jnxL2cpMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxL2cpMibRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Counter64, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, TimeTicks, ModuleIdentity, Counter32, NotificationType, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Counter64", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "TimeTicks", "ModuleIdentity", "Counter32", "NotificationType", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
jnxL2cpFeaturesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1))
jnxL2cpFeaturesMIB.setRevisions(('2012-06-25 00:00', '2012-08-15 00:00', '2010-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxL2cpFeaturesMIB.setRevisionsDescriptions(('Modifying max access for LacpTimeOut trap objects.', 'Added new mib jnxLacpAggTimeout.', 'Added new trap jnxLacpTimeOut.',))
if mibBuilder.loadTexts: jnxL2cpFeaturesMIB.setLastUpdated('201206250000Z')
if mibBuilder.loadTexts: jnxL2cpFeaturesMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxL2cpFeaturesMIB.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxL2cpFeaturesMIB.setDescription('This mib module is for Juniper Networks Proprietory Layer 2 control protocol (L2CP) features')
jnxL2cpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1))
jnxL2cpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2))
jnxL2cpStpProtectObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1))
jnxL2cpBpduProtectObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 2))
jnxDot1dStpPortProtectTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1, 1), )
if mibBuilder.loadTexts: jnxDot1dStpPortProtectTable.setStatus('current')
if mibBuilder.loadTexts: jnxDot1dStpPortProtectTable.setDescription('Defines the jnxDot1dStp Port Table for providing enterprise specific extensions for Root Protect and Loop Protect to the corresponding dot1dStpPortTable entry.')
jnxDot1dStpPortProtectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1, 1, 1), )
dot1dStpPortEntry.registerAugmentions(("JUNIPER-L2CP-FEATURES-MIB", "jnxDot1dStpPortProtectEntry"))
jnxDot1dStpPortProtectEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
if mibBuilder.loadTexts: jnxDot1dStpPortProtectEntry.setStatus('current')
if mibBuilder.loadTexts: jnxDot1dStpPortProtectEntry.setDescription('Defines an entry in the jnxDot1dStpPortProtectTable. This essentially augments the dot1dStpPortTable with additional objects.')
jnxDot1dStpPortRootProtectEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxDot1dStpPortRootProtectEnabled.setStatus('current')
if mibBuilder.loadTexts: jnxDot1dStpPortRootProtectEnabled.setDescription('A Boolean value set by management indicating whether Root protect functionality is enabled on the port. If TRUE causes the Port not to be selected as Root Port, even it has the best spanning tree priority vector. This parameter should be FALSE by default. ')
jnxDot1dStpPortRootProtectState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no-error", 0), ("root-prevented", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxDot1dStpPortRootProtectState.setStatus('current')
if mibBuilder.loadTexts: jnxDot1dStpPortRootProtectState.setDescription("Indicates whether the port was prevented from being a root port. This parameter will always return 'no-error (0)' if jnxDot1dStpPortRootProtectEnabled is FALSE. ")
jnxDot1dStpPortLoopProtectEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxDot1dStpPortLoopProtectEnabled.setStatus('current')
if mibBuilder.loadTexts: jnxDot1dStpPortLoopProtectEnabled.setDescription('A Boolean value set by management indicating whether Loop protect functionality is enabled on the port. If TRUE causes the Port not to be selected as Designated Port when the received superior BPDU is aged out. This parameter should be FALSE by default. ')
jnxDot1dStpPortLoopProtectState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no-error", 0), ("loop-prevented", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxDot1dStpPortLoopProtectState.setStatus('current')
if mibBuilder.loadTexts: jnxDot1dStpPortLoopProtectState.setDescription("Indicates whether a potential Loop was prevented on the port This parameter will always return 'no-error (0)' if jnxDot1dStpPortLoopProtectEnabled is FALSE. ")
jnxL2cpBpduProtectPortTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 2, 1), )
if mibBuilder.loadTexts: jnxL2cpBpduProtectPortTable.setStatus('current')
if mibBuilder.loadTexts: jnxL2cpBpduProtectPortTable.setDescription('Defines a Port Table for BPDU Protect information. This contains only those ports on which BPDU Protect can be configured.')
jnxL2cpBpduProtectPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxL2cpBpduProtectPortEntry.setStatus('current')
if mibBuilder.loadTexts: jnxL2cpBpduProtectPortEntry.setDescription('Defines an entry in the jnxL2cpBpduProtectPortTable. A list containing BPDU Protect information for each Port.')
jnxL2cpBpduProtectPortEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2cpBpduProtectPortEnabled.setStatus('current')
if mibBuilder.loadTexts: jnxL2cpBpduProtectPortEnabled.setDescription('A Boolean value set by management indicating whether BPDU protect functionality is enabled on the port. If TRUE causes the Port to be disabled (link down) upon receipt of a BPDU. This parameter should be FALSE by default. ')
jnxL2cpPortBpduError = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no-error", 0), ("detected", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2cpPortBpduError.setStatus('current')
if mibBuilder.loadTexts: jnxL2cpPortBpduError.setDescription("Indicates whether a BPDU was received on the port. This parameter will always return 'no-error (0)' if jnxL2cpBpduProtectPortEnabled is FALSE. ")
jnxL2cpBpduProtectDisableTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2cpBpduProtectDisableTimeout.setStatus('current')
if mibBuilder.loadTexts: jnxL2cpBpduProtectDisableTimeout.setDescription('Returns the value of time (in seconds) after which a port on which BPDU error was detected will be re-enabled. A returned value of 0 indicates that port will not be re-enabled automatically.')
jnxL2cpProtectTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2, 0))
jnxPortRootProtectStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2, 0, 1)).setObjects(("JUNIPER-L2CP-FEATURES-MIB", "jnxDot1dStpPortRootProtectState"))
if mibBuilder.loadTexts: jnxPortRootProtectStateChangeTrap.setStatus('current')
if mibBuilder.loadTexts: jnxPortRootProtectStateChangeTrap.setDescription('Generated when the ports Root-protect state (no-error or root-prevented) changes.')
jnxPortLoopProtectStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2, 0, 2)).setObjects(("JUNIPER-L2CP-FEATURES-MIB", "jnxDot1dStpPortLoopProtectState"))
if mibBuilder.loadTexts: jnxPortLoopProtectStateChangeTrap.setStatus('current')
if mibBuilder.loadTexts: jnxPortLoopProtectStateChangeTrap.setDescription('Generated when the ports Loop-protect state (no-error or loop-prevented) changes.')
jnxPortBpduErrorStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2, 0, 3)).setObjects(("JUNIPER-L2CP-FEATURES-MIB", "jnxL2cpPortBpduError"))
if mibBuilder.loadTexts: jnxPortBpduErrorStatusChangeTrap.setStatus('current')
if mibBuilder.loadTexts: jnxPortBpduErrorStatusChangeTrap.setDescription('Generated when the ports BPDU error state (no-error or detected) changes.')
jnxLacpNotifyVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 3))
jnxLacpAggTimeout = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4))
jnxLacpNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2, 1))
class LacpState(TextualConvention, Bits):
    description = 'The Actor and Partner State values from the LACPDU.'
    status = 'current'
    namedValues = NamedValues(("lacpActivity", 0), ("lacpTimeout", 1), ("aggregation", 2), ("synchronization", 3), ("collecting", 4), ("distributing", 5), ("defaulted", 6), ("expired", 7))

jnxLacpInterfaceName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 3, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxLacpInterfaceName.setStatus('current')
if mibBuilder.loadTexts: jnxLacpInterfaceName.setDescription('Lacp member interface.')
jnxLacpifIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 3, 2), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxLacpifIndex.setStatus('current')
if mibBuilder.loadTexts: jnxLacpifIndex.setDescription('Snmp ifIndex of member interface.')
jnxLacpAggregateInterfaceName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 3, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxLacpAggregateInterfaceName.setStatus('current')
if mibBuilder.loadTexts: jnxLacpAggregateInterfaceName.setDescription('Lacp Aggregate interface.')
jnxLacpAggregateifIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 3, 4), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxLacpAggregateifIndex.setStatus('current')
if mibBuilder.loadTexts: jnxLacpAggregateifIndex.setDescription('Snmp ifIndex of Aggregator.')
jnxLacpAggPortActorOperState = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 3, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxLacpAggPortActorOperState.setStatus('current')
if mibBuilder.loadTexts: jnxLacpAggPortActorOperState.setDescription('Port actor operational state.')
jnxLacpTimeOut = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 2, 1, 1)).setObjects(("JUNIPER-L2CP-FEATURES-MIB", "jnxLacpInterfaceName"), ("JUNIPER-L2CP-FEATURES-MIB", "jnxLacpifIndex"), ("JUNIPER-L2CP-FEATURES-MIB", "jnxLacpAggregateInterfaceName"), ("JUNIPER-L2CP-FEATURES-MIB", "jnxLacpAggregateifIndex"), ("JUNIPER-L2CP-FEATURES-MIB", "jnxLacpAggPortActorOperState"))
if mibBuilder.loadTexts: jnxLacpTimeOut.setStatus('current')
if mibBuilder.loadTexts: jnxLacpTimeOut.setDescription('Lacp times out')
dot3adAggPortTimeoutTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4, 1), )
if mibBuilder.loadTexts: dot3adAggPortTimeoutTable.setReference('IEEE 802.3')
if mibBuilder.loadTexts: dot3adAggPortTimeoutTable.setStatus('current')
if mibBuilder.loadTexts: dot3adAggPortTimeoutTable.setDescription('A table that contains Link Aggregation Timeout information about a port that is associated with this device. A row appears in this table for each physical port.')
dot3adAggPortTimeoutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3adAggPortTimeoutEntry.setStatus('current')
if mibBuilder.loadTexts: dot3adAggPortTimeoutEntry.setDescription('A list of Link Aggregation Control Protocol timeout information for a port on this device.')
dot3adInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adInterfaceName.setReference('IEEE 802.3')
if mibBuilder.loadTexts: dot3adInterfaceName.setStatus('current')
if mibBuilder.loadTexts: dot3adInterfaceName.setDescription('Physical port that is associated with Aggregation Port. This value is read-only.')
dot3adOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4, 1, 1, 2), LacpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adOperState.setReference('IEEE 802.3 Subclause 30.7.2.1.21')
if mibBuilder.loadTexts: dot3adOperState.setStatus('current')
if mibBuilder.loadTexts: dot3adOperState.setDescription('A string of 8 bits, corresponding to the current operational values of Actor_State as transmitted by the Actor in LACPDUs. The bit allocations are as defined in 30.7.2.1.20. This attribute value is read-only.')
dot3adAggname = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggname.setReference('IEEE 802.3')
if mibBuilder.loadTexts: dot3adAggname.setStatus('current')
if mibBuilder.loadTexts: dot3adAggname.setDescription('Aggregation Port where Physical port is associated with. This value is read-only.')
dot3adInterfaceTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 53, 1, 1, 4, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adInterfaceTimeout.setReference('IEEE 802.3')
if mibBuilder.loadTexts: dot3adInterfaceTimeout.setStatus('current')
if mibBuilder.loadTexts: dot3adInterfaceTimeout.setDescription('This object represents the time elapsed in seconds since lacp experienced timeout. This value is read-only.')
mibBuilder.exportSymbols("JUNIPER-L2CP-FEATURES-MIB", jnxLacpNotificationsPrefix=jnxLacpNotificationsPrefix, jnxLacpTimeOut=jnxLacpTimeOut, jnxLacpAggregateifIndex=jnxLacpAggregateifIndex, dot3adAggname=dot3adAggname, jnxL2cpPortBpduError=jnxL2cpPortBpduError, jnxL2cpNotifications=jnxL2cpNotifications, dot3adInterfaceName=dot3adInterfaceName, jnxL2cpBpduProtectPortTable=jnxL2cpBpduProtectPortTable, jnxL2cpBpduProtectPortEntry=jnxL2cpBpduProtectPortEntry, jnxL2cpBpduProtectDisableTimeout=jnxL2cpBpduProtectDisableTimeout, jnxL2cpBpduProtectPortEnabled=jnxL2cpBpduProtectPortEnabled, dot3adOperState=dot3adOperState, jnxDot1dStpPortRootProtectEnabled=jnxDot1dStpPortRootProtectEnabled, jnxL2cpProtectTraps=jnxL2cpProtectTraps, jnxDot1dStpPortLoopProtectEnabled=jnxDot1dStpPortLoopProtectEnabled, dot3adAggPortTimeoutTable=dot3adAggPortTimeoutTable, jnxDot1dStpPortRootProtectState=jnxDot1dStpPortRootProtectState, dot3adAggPortTimeoutEntry=dot3adAggPortTimeoutEntry, jnxLacpifIndex=jnxLacpifIndex, jnxL2cpBpduProtectObjects=jnxL2cpBpduProtectObjects, LacpState=LacpState, jnxLacpAggPortActorOperState=jnxLacpAggPortActorOperState, jnxDot1dStpPortProtectTable=jnxDot1dStpPortProtectTable, jnxPortRootProtectStateChangeTrap=jnxPortRootProtectStateChangeTrap, jnxDot1dStpPortLoopProtectState=jnxDot1dStpPortLoopProtectState, jnxPortLoopProtectStateChangeTrap=jnxPortLoopProtectStateChangeTrap, jnxLacpNotifyVars=jnxLacpNotifyVars, jnxLacpAggregateInterfaceName=jnxLacpAggregateInterfaceName, jnxLacpAggTimeout=jnxLacpAggTimeout, dot3adInterfaceTimeout=dot3adInterfaceTimeout, jnxPortBpduErrorStatusChangeTrap=jnxPortBpduErrorStatusChangeTrap, jnxL2cpFeaturesMIB=jnxL2cpFeaturesMIB, jnxL2cpStpProtectObjects=jnxL2cpStpProtectObjects, jnxDot1dStpPortProtectEntry=jnxDot1dStpPortProtectEntry, jnxLacpInterfaceName=jnxLacpInterfaceName, PYSNMP_MODULE_ID=jnxL2cpFeaturesMIB, jnxL2cpObjects=jnxL2cpObjects)
