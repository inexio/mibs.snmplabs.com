#
# PySNMP MIB module JUNIPER-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:01:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
jnxMibs, jnxSyslogNotifications = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs", "jnxSyslogNotifications")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Unsigned32, Counter64, Bits, TimeTicks, Counter32, ObjectIdentity, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Unsigned32", "Counter64", "Bits", "TimeTicks", "Counter32", "ObjectIdentity", "MibIdentifier", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
jnxSyslog = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 35))
if mibBuilder.loadTexts: jnxSyslog.setLastUpdated('200603202153Z')
if mibBuilder.loadTexts: jnxSyslog.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxSyslog.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxSyslog.setDescription('This is Juniper Networks implementation of enterprise specific MIB for syslogs generated by JUNOS.')
class JnxSyslogSeverity(TextualConvention, Integer32):
    description = 'The severity of the generated syslog message. The enumeration values are equal to the values that syslog uses + 1. For example, with syslog, emergency=0.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))

class JnxSyslogFacility(TextualConvention, Integer32):
    description = 'The facility of the generated syslog message.The enumeration values are equal to the values that syslog uses + 1. For example, with syslog, kernel=0.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("kernel", 1), ("user", 2), ("mail", 3), ("daemon", 4), ("auth", 5), ("syslog", 6), ("lpr", 7), ("news", 8), ("uucp", 9), ("cron", 10), ("authPriv", 11), ("ftp", 12), ("ntp", 13), ("security", 14), ("console", 15), ("local0", 17), ("dfc", 18), ("local2", 19), ("firewall", 20), ("pfe", 21), ("conflict", 22), ("change", 23), ("interact", 24))

jnxSyslogNotifyVars = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1))
if mibBuilder.loadTexts: jnxSyslogNotifyVars.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogNotifyVars.setDescription('Notification object definitions.')
jnxSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1), )
if mibBuilder.loadTexts: jnxSyslogTable.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogTable.setDescription('A table of syslog messages generated by the device.')
jnxSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1), ).setIndexNames((0, "JUNIPER-SYSLOG-MIB", "jnxSyslogId"))
if mibBuilder.loadTexts: jnxSyslogEntry.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogEntry.setDescription('An entry of syslog table.')
jnxSyslogId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: jnxSyslogId.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogId.setDescription('Syslog message identifier. This is also used as primary index in jnxSyslogAttrValTable')
jnxSyslogEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSyslogEventName.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogEventName.setDescription('An octet string containing syslog event name.')
jnxSyslogTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 3), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSyslogTimestamp.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogTimestamp.setDescription('Date and Time of syslog message generation.')
jnxSyslogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 4), JnxSyslogSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSyslogSeverity.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogSeverity.setDescription('Identifies the severity of this syslog message.')
jnxSyslogFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 5), JnxSyslogFacility()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSyslogFacility.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogFacility.setDescription('Identified the facility of this syslog message.')
jnxSyslogProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 6), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSyslogProcessId.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogProcessId.setDescription('Process-Id of the process that generated this syslog message.')
jnxSyslogProcessName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSyslogProcessName.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogProcessName.setDescription('Name of the process that generated this syslog message.')
jnxSyslogHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 8), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSyslogHostName.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogHostName.setDescription('Hostname of host on which this syslog message is generated.')
jnxSyslogMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 9), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSyslogMessage.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogMessage.setDescription('The syslog message string.')
jnxSyslogAvTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2), )
if mibBuilder.loadTexts: jnxSyslogAvTable.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogAvTable.setDescription('A table of attribute value pairs of the syslog messages generated by the device.')
jnxSyslogAvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2, 1), ).setIndexNames((0, "JUNIPER-SYSLOG-MIB", "jnxSyslogId"), (0, "JUNIPER-SYSLOG-MIB", "jnxSyslogAvIndex"))
if mibBuilder.loadTexts: jnxSyslogAvEntry.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogAvEntry.setDescription('An entry of attribute value pair.')
jnxSyslogAvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: jnxSyslogAvIndex.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogAvIndex.setDescription('Identifies the sequence number of attribute-value pair in the syslog message.')
jnxSyslogAvAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSyslogAvAttribute.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogAvAttribute.setDescription('Attribute of the syslog message identified by jnxSyslogId.')
jnxSyslogAvValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSyslogAvValue.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogAvValue.setDescription('Value of the attribute identified by jnxSyslogAvAttribute.')
jnxSyslogNotificationPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 4, 12, 0))
if mibBuilder.loadTexts: jnxSyslogNotificationPrefix.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogNotificationPrefix.setDescription('All Syslog notifications are registered under this branch.')
jnxSyslogTrap = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 12, 0, 1)).setObjects(("JUNIPER-SYSLOG-MIB", "jnxSyslogEventName"), ("JUNIPER-SYSLOG-MIB", "jnxSyslogTimestamp"), ("JUNIPER-SYSLOG-MIB", "jnxSyslogSeverity"), ("JUNIPER-SYSLOG-MIB", "jnxSyslogFacility"), ("JUNIPER-SYSLOG-MIB", "jnxSyslogProcessId"), ("JUNIPER-SYSLOG-MIB", "jnxSyslogProcessName"), ("JUNIPER-SYSLOG-MIB", "jnxSyslogHostName"), ("JUNIPER-SYSLOG-MIB", "jnxSyslogMessage"))
if mibBuilder.loadTexts: jnxSyslogTrap.setStatus('current')
if mibBuilder.loadTexts: jnxSyslogTrap.setDescription('Notification of a generated syslog message. Apart from the jnxSyslogTrap objects, this notification can include one or more attribute-value pairs. The attribute-value pairs shall be identified by objects jnxSyslogAvAttribute and jnxSyslogAvValue.')
mibBuilder.exportSymbols("JUNIPER-SYSLOG-MIB", JnxSyslogFacility=JnxSyslogFacility, jnxSyslogAvTable=jnxSyslogAvTable, jnxSyslogMessage=jnxSyslogMessage, jnxSyslogNotifyVars=jnxSyslogNotifyVars, JnxSyslogSeverity=JnxSyslogSeverity, jnxSyslogEntry=jnxSyslogEntry, jnxSyslogEventName=jnxSyslogEventName, jnxSyslogAvEntry=jnxSyslogAvEntry, jnxSyslogSeverity=jnxSyslogSeverity, jnxSyslogAvAttribute=jnxSyslogAvAttribute, jnxSyslogNotificationPrefix=jnxSyslogNotificationPrefix, jnxSyslogId=jnxSyslogId, jnxSyslogTrap=jnxSyslogTrap, jnxSyslogHostName=jnxSyslogHostName, PYSNMP_MODULE_ID=jnxSyslog, jnxSyslogAvValue=jnxSyslogAvValue, jnxSyslogProcessName=jnxSyslogProcessName, jnxSyslogTimestamp=jnxSyslogTimestamp, jnxSyslog=jnxSyslog, jnxSyslogTable=jnxSyslogTable, jnxSyslogProcessId=jnxSyslogProcessId, jnxSyslogAvIndex=jnxSyslogAvIndex, jnxSyslogFacility=jnxSyslogFacility)
