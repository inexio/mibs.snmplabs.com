#
# PySNMP MIB module ENTERASYS-DIAGNOSTIC-MESSAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-DIAGNOSTIC-MESSAGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:03:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, Counter32, ObjectIdentity, Bits, Unsigned32, TimeTicks, Counter64, Gauge32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "ObjectIdentity", "Bits", "Unsigned32", "TimeTicks", "Counter64", "Gauge32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Integer32")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
etsysDiagnosticMessageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13))
etsysDiagnosticMessageMIB.setRevisions(('2003-01-10 21:17', '2002-06-07 14:28', '2001-12-03 19:51', '2001-08-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysDiagnosticMessageMIB.setRevisionsDescriptions(('Added a textual convention to provide a display hint for the etsysDiagnosticMessageDetailsText object.', 'Added Enterasys copyright notice and corrected some text.', 'Removed the import of BITS from SNMPv2-SMI.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysDiagnosticMessageMIB.setLastUpdated('200304252048Z')
if mibBuilder.loadTexts: etsysDiagnosticMessageMIB.setOrganization('Enterasys Networks')
if mibBuilder.loadTexts: etsysDiagnosticMessageMIB.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysDiagnosticMessageMIB.setDescription('This MIB module defines a portion of the SNMP enterprise MIBs under the Enterasys enterprise OID pertaining to the retrieval of diagnostic messages.')
class LongAdminString(TextualConvention, OctetString):
    reference = 'RFC2571 (An Architecture for Describing SNMP Management Frameworks)'
    description = 'A size extended version of an SnmpAdminString as defined in RFC2571. '
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

etsysDiagnosticMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1))
etsysDiagnosticMessageDetails = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2))
etsysDiagnosticMessageCount = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageCount.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageCount.setDescription('The number of messages logged on this entity since the beginning of time. This value must be persistent. There should be no facility to clear this value.')
etsysDiagnosticMessageChanges = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageChanges.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageChanges.setDescription('The number of changes to the message log since the last reboot. Changes should include, clearing the message log, deleting a message, and the logging of new messages.')
etsysDiagnosticMessageTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3), )
if mibBuilder.loadTexts: etsysDiagnosticMessageTable.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageTable.setDescription('This table lists a summary of the diagnostic messages stored on the managed entity.')
etsysDiagnosticMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1), ).setIndexNames((0, "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageIndex"))
if mibBuilder.loadTexts: etsysDiagnosticMessageEntry.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageEntry.setDescription('An entry describing a particular diagnostic message. Every message that is stored in non-volatile memory is required to appear in this table.')
etsysDiagnosticMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: etsysDiagnosticMessageIndex.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageIndex.setDescription('A unique arbitrary identifier for this message. For stateless message log implementations it may be valid only while etsysDiagnosticMessageChanges remains unchanged.')
etsysDiagnosticMessageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageTime.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageTime.setDescription('The time and date that this message was stored.')
etsysDiagnosticMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageType.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageType.setDescription('A description of the type of message shown in this entry.')
etsysDiagnosticMessageSummary = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageSummary.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageSummary.setDescription('A brief summary of the diagnostic message.')
etsysDiagnosticMessageFWRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageFWRevision.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageFWRevision.setDescription('The string representing the version of firmware running on the the managed entity at the time the message was stored.')
etsysDiagnosticMessageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 6), Bits().clone(namedValues=NamedValues(("etsysDiagnosticMessageBadChecksum", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageStatus.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageStatus.setDescription('A list of attributes associated with this message. Generally these attributes would be considered exceptional, but could potentially be extended to indicate any number of conditions.')
etsysDiagnosticMessageDetailsTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1), )
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsTable.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsTable.setDescription('This table contains the complete diagnostic messages for entries in the etsysDiagnosticMessageSummaryTable. This allows a message of virtually unlimited length to be accessible via SNMP.')
etsysDiagnosticMessageDetailsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1), ).setIndexNames((0, "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageIndex"), (0, "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageDetailsIndex"))
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsEntry.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsEntry.setDescription('An entry describing a particular fragment of a message.')
etsysDiagnosticMessageDetailsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsIndex.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsIndex.setDescription("A unique arbitrary identifier for this message fragment. Ideally this index should have the values 1 - n, where 'n' is the number of message fragments. It, at a minimum, must be chosen such that the lexicographical ordering will allow the fragments to be assembled in the proper order.")
etsysDiagnosticMessageDetailsText = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1, 2), LongAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsText.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsText.setDescription('The text that makes up a fragment of a message.')
etsysDiagnosticMessageDetailsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1, 3), Bits().clone(namedValues=NamedValues(("etsysDiagnosticMessageLastSegment", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsStatus.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsStatus.setDescription('A list of attributes associated with this message segment.')
etsysDiagnosticMessageConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3))
etsysDiagnosticMessageGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 1))
etsysDiagnosticMessageCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 2))
etsysDiagnosticMessageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 1, 1)).setObjects(("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageCount"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageChanges"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageTime"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageType"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageSummary"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageFWRevision"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageStatus"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageDetailsText"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageDetailsStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDiagnosticMessageGroup = etsysDiagnosticMessageGroup.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageGroup.setDescription('The basic etsysDiagnosticMessage group.')
etsysDiagnosticMessageCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 2, 1)).setObjects(("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDiagnosticMessageCompliance = etsysDiagnosticMessageCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysDiagnosticMessageCompliance.setDescription('The compliance statement for managed entities that support diagnostic message logs.')
mibBuilder.exportSymbols("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", etsysDiagnosticMessageDetailsText=etsysDiagnosticMessageDetailsText, etsysDiagnosticMessageTime=etsysDiagnosticMessageTime, PYSNMP_MODULE_ID=etsysDiagnosticMessageMIB, etsysDiagnosticMessageEntry=etsysDiagnosticMessageEntry, etsysDiagnosticMessageDetails=etsysDiagnosticMessageDetails, LongAdminString=LongAdminString, etsysDiagnosticMessageCompliance=etsysDiagnosticMessageCompliance, etsysDiagnosticMessageCount=etsysDiagnosticMessageCount, etsysDiagnosticMessageSummary=etsysDiagnosticMessageSummary, etsysDiagnosticMessageType=etsysDiagnosticMessageType, etsysDiagnosticMessageMIB=etsysDiagnosticMessageMIB, etsysDiagnosticMessageFWRevision=etsysDiagnosticMessageFWRevision, etsysDiagnosticMessage=etsysDiagnosticMessage, etsysDiagnosticMessageTable=etsysDiagnosticMessageTable, etsysDiagnosticMessageDetailsTable=etsysDiagnosticMessageDetailsTable, etsysDiagnosticMessageDetailsStatus=etsysDiagnosticMessageDetailsStatus, etsysDiagnosticMessageCompliances=etsysDiagnosticMessageCompliances, etsysDiagnosticMessageStatus=etsysDiagnosticMessageStatus, etsysDiagnosticMessageGroups=etsysDiagnosticMessageGroups, etsysDiagnosticMessageDetailsEntry=etsysDiagnosticMessageDetailsEntry, etsysDiagnosticMessageChanges=etsysDiagnosticMessageChanges, etsysDiagnosticMessageConformance=etsysDiagnosticMessageConformance, etsysDiagnosticMessageIndex=etsysDiagnosticMessageIndex, etsysDiagnosticMessageDetailsIndex=etsysDiagnosticMessageDetailsIndex, etsysDiagnosticMessageGroup=etsysDiagnosticMessageGroup)
