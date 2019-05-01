#
# PySNMP MIB module APPIAN-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APPIAN-SMI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:09:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, enterprises, Integer32, ModuleIdentity, NotificationType, Gauge32, Unsigned32, Counter32, Bits, IpAddress, Counter64, iso, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "enterprises", "Integer32", "ModuleIdentity", "NotificationType", "Gauge32", "Unsigned32", "Counter32", "Bits", "IpAddress", "Counter64", "iso", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
appian = ModuleIdentity((1, 3, 6, 1, 4, 1, 2785))
appian.setRevisions(('1900-01-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: appian.setRevisionsDescriptions(('Draft engineering version. Not for release.',))
if mibBuilder.loadTexts: appian.setLastUpdated('0001270000Z')
if mibBuilder.loadTexts: appian.setOrganization('Appian Communications, Inc.')
if mibBuilder.loadTexts: appian.setContactInfo('Douglas Theriault')
if mibBuilder.loadTexts: appian.setDescription('Appian Communications Enterprise MIB Definitions')
class AcAdminStatus(TextualConvention, Integer32):
    description = 'It triggers the specified administrative action on a set of scalars or on a row in a table. activate(1) triggers the activation of a set of scalars or a row in a table. delete(2) triggers the deletion of a row in a table. inactivate(3) inactivates a set of scalars or a row in a table. The remaining enumerations listed below are for the generation of Traps used by the Appian SNMP Agent Simulator. These enumerations are not expected to be included when we ship our final enterprise MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("activate", 1), ("delete", 2), ("inactivate", 3))

class AcOpStatus(TextualConvention, Integer32):
    description = 'It describes the operability of a resource. Permitted values are: operational: the resource is partially or fully operable and available for use. offline: the resource requires a routine operation to be performed to place it online and make it available for use. initializing: the resource is undergoing initialization. selfTesting: the resource is undergoing a self-test procedure. provisioning: the resource is being provisioned. upgrading: the resource software, if applicable, is being upgraded. maintenance: the resource is currently under maintenance. standby: the resource is not providing service, but will take over the role of an associated operational resource if the latter fails. shuttingDown: the resource is in a termination phase. failed: the resource has an internal fault that prevents it from operating. hw-not-present: the resource has no hardware to provide service.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("operational", 1), ("offline", 2), ("initializing", 3), ("selfTesting", 4), ("provisioning", 5), ("upgrading", 6), ("maintenance", 7), ("standby", 8), ("shuttingDown", 9), ("failed", 10), ("hw-not-present", 11))

class AcSlotNumber(TextualConvention, Integer32):
    description = 'A physical slot number in an OSAP Chassis which is within the range of (1..16). Or the value 100 to indicate an Ethernet port group.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 100))
    namedValues = NamedValues(("ac0", 0), ("ac1", 1), ("ac2", 2), ("ac3", 3), ("ac4", 4), ("ac5", 5), ("ac6", 6), ("ac7", 7), ("ac8", 8), ("ac9", 9), ("ac10", 10), ("ac11", 11), ("ac12", 12), ("ac13", 13), ("ac14", 14), ("ac15", 15), ("ac16", 16), ("ac100", 100))

class AcPortNumber(TextualConvention, Integer32):
    description = 'A physical port number on a media i/o card which is within the range of (1..8).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8)

class AcLastChange(TextualConvention, TimeTicks):
    description = "The last 'time' an entity is modified. The entity could be a single MIB object or a MIB table. For a table, modification to any objects in the table would apply. The last time is defined as the sysUpTime when the modification took place. The modification could be triggered by management systems, CLI commands, parameter synchronization and distribution protocols, and others. If there were no modification, it should have the value of 0."
    status = 'current'

class AcMibVersion(DisplayString):
    description = "An ASCII string which identifies the major and minor version of the Appian MIB currently supported by the active switch control processor. The format for this string is '<major>.<minor>'. The string will support up to 9 characters in length. The major.minor numbers are derived from the active switch controllers software version."
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 9)

class AcSwVersion(DisplayString):
    description = "An ASCII string which identifies the major and minor version of the Appian software running on one or more modules within the chassis. The format for this string is '<major>.<minor>.<patch>.<build>'. The string will support up to 19 characters in length."
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 19)

class AcNodeId(TextualConvention, Integer32):
    description = 'A unique value assigned to each OSAP in a ring by the EMS system. This is used in our MIB tables as part of an instance identifier so we can enable management of the ring as a single entity from any OSAP within the ring.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class AcRingId(TextualConvention, Integer32):
    description = 'A unique value assigned to each Appian Ring by the EMS system. This is used in trap messages to help manage the event messages generated by a network of Appian Rings. The number is rather large, and with a max of 16 or so nodes per ring gives an upper bound to the network to be approx. 1*10^6 nodes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class AcNodeArchitecture(TextualConvention, Integer32):
    description = 'This value describes where this node is in the network. The value describes the network/ring from the perspective of the node, not the network. * unconfigured: The node architecture has not been configured. * linear: The node is in a linear configuration. * ring: The node is part of a ring. * ring-interconnect: The node is in a ring and is used as the interconnect. * drop-and-continue-pri: The node is the primary in a drop and continue architecture. * drop-and-continue-sec: The node is the secondary in a drop and continue architecture. * subtending-pri: The node is the primary in a subtending ring architecture. * subtending-sec: The node is the secondary in a subtending ring architecture.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unconfigured", 0), ("linear", 1), ("ring", 2), ("ring-interconnect", 3), ("drop-and-continue-pri", 4), ("drop-and-continue-sec", 5), ("subtending-pri", 6), ("subtending-sec", 7))

acIdentifier = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 1))
acProductId = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 1, 1))
acOsap = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2))
acPport = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2, 3))
acLport = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2, 4))
acTrunks = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2, 6))
acServices = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2, 8))
mibBuilder.exportSymbols("APPIAN-SMI-MIB", acLport=acLport, acIdentifier=acIdentifier, acServices=acServices, AcAdminStatus=AcAdminStatus, acPport=acPport, AcNodeId=AcNodeId, AcMibVersion=AcMibVersion, acOsap=acOsap, AcPortNumber=AcPortNumber, AcOpStatus=AcOpStatus, acTrunks=acTrunks, appian=appian, AcSwVersion=AcSwVersion, acProductId=acProductId, AcNodeArchitecture=AcNodeArchitecture, PYSNMP_MODULE_ID=appian, AcLastChange=AcLastChange, AcSlotNumber=AcSlotNumber, AcRingId=AcRingId)
