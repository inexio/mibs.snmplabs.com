#
# PySNMP MIB module CTRON-ENTITY-STATE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-ENTITY-STATE-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:29:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ctEntityStateTC, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctEntityStateTC")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, NotificationType, Integer32, ModuleIdentity, iso, TimeTicks, Unsigned32, ObjectIdentity, Counter32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "NotificationType", "Integer32", "ModuleIdentity", "iso", "TimeTicks", "Unsigned32", "ObjectIdentity", "Counter32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctEntityStateTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 2, 30, 1))
ctEntityStateTc.setRevisions(('2005-01-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ctEntityStateTc.setRevisionsDescriptions(('Initial version, published as RFC yyyy.',))
if mibBuilder.loadTexts: ctEntityStateTc.setLastUpdated('200501230000Z')
if mibBuilder.loadTexts: ctEntityStateTc.setOrganization('IETF Entity MIB Working Group')
if mibBuilder.loadTexts: ctEntityStateTc.setContactInfo('General Discussion: entmib@ietf.org To Subscribe: http://www.ietf.org/mailman/listinfo/entmib http://www.ietf.org/html.charters/entmib-charter.html Sharon Chisholm Nortel Networks PO Box 3511 Station C Ottawa, Ont. K1Y 4H7 Canada schishol@nortelnetworks.com David T. Perkins 548 Qualbrook Ct San Jose, CA 95110 USA Phone: 408 394-8702 dperkins@snmpinfo.com')
if mibBuilder.loadTexts: ctEntityStateTc.setDescription('This MIB defines state textual conventions. Copyright (C) The Internet Society 2005. This version of this MIB module is part of RFC yyyy; see the RFC itself for full legal notices.')
class EntityAdminState(TextualConvention, Integer32):
    description = " Represents the various possible administrative states. A value of 'locked' means the resource is administratively prohibited from use. A value of 'shuttingDown' means that usage is administratively limited to current instances of use. A value of 'unlocked' means the resource is not administratively prohibited from use. A value of 'unknown' means that this resource is unable to report administrative state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("locked", 2), ("shuttingDown", 3), ("unlocked", 4))

class EntityOperState(TextualConvention, Integer32):
    description = " Represents the possible values of operational states. A value of 'disabled' means the resource is totally inoperable. A value of 'enabled' means the resource is partially or fully operable. A value of 'testing' means the resource is currently being tested and cannot therefore report whether it is operational or not. A value of 'unknown' means that this resource is unable to report operational state. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3), ("testing", 4))

class EntityUsageState(TextualConvention, Integer32):
    description = " Represents the possible values of usage states. A value of 'idle' means the resource is servicing no users. A value of 'active' means the resource is currently in use and it has sufficient spare capacity to provide for additional users. A value of 'busy' means the resource is currently in use, but it currently has no spare capacity to provide for additional users. A value of 'unknown' means that this resource is unable to report usage state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("idle", 2), ("active", 3), ("busy", 4))

class EntityAlarmStatus(TextualConvention, Bits):
    description = "Represents the possible values of alarm status. An Alarm [RFC3877] is a persistent indication of an error or warning condition. When no bits of this attribute are set, then no active alarms are known against this entity and it is not under repair. When the 'value of underRepair' is set, the resource is currently being repaired, which, depending on the implementation, may make the other values in this bit string not meaningful. When the value of 'critical' is set, one or more critical alarms are active against the resource. When the value of 'major' is set, one or more major alarms are active against the resource. When the value of 'minor' is set, one or more minor alarms are active against the resource. When the value of 'warning' is set, one or more warning alarms are active against the resource. When the value of 'indeterminate' is set, one or more alarms whose of perceived severity cannot be determined are active against this resource. A value of 'unknown' means that this resource is unable to report alarm state."
    status = 'current'
    namedValues = NamedValues(("unknown", 0), ("underRepair", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("indeterminate", 6))

class EntityStandbyStatus(TextualConvention, Integer32):
    description = " Represents the possible values of standby status. A value of 'hotStandby' means the resource is not providing service, but it will be immediately able to take over the role of the resource to be backed-up, without the need for initialization activity, and will contain the same information as the resource to be backed up. A value of 'coldStandy' means that the resource is to back-up another resource, but will not be immediately able to take over the role of a resource to be backed up, and will require some initialization activity. A value of 'providingService' means the resource is providing service. A value of 'unknown' means that this resource is unable to report standby state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("hotStandby", 2), ("coldStandby", 3), ("providingService", 4))

mibBuilder.exportSymbols("CTRON-ENTITY-STATE-TC-MIB", ctEntityStateTc=ctEntityStateTc, EntityStandbyStatus=EntityStandbyStatus, EntityOperState=EntityOperState, EntityUsageState=EntityUsageState, EntityAdminState=EntityAdminState, PYSNMP_MODULE_ID=ctEntityStateTc, EntityAlarmStatus=EntityAlarmStatus)
