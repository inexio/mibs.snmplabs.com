#
# PySNMP MIB module APACHE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APACHE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:23:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, MibIdentifier, Bits, TimeTicks, Counter64, Gauge32, Integer32, enterprises, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "MibIdentifier", "Bits", "TimeTicks", "Counter64", "Gauge32", "Integer32", "enterprises", "NotificationType", "Counter32")
TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString")
apacheMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4))
apacheMIB.setRevisions(('1998-10-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: apacheMIB.setRevisionsDescriptions(('The intial version.',))
if mibBuilder.loadTexts: apacheMIB.setLastUpdated('9810010000Z')
if mibBuilder.loadTexts: apacheMIB.setOrganization('Harrie hazewinkel')
if mibBuilder.loadTexts: apacheMIB.setContactInfo('Harrie Hazewinkel email: harrie.hazewinkel@jrc.it')
if mibBuilder.loadTexts: apacheMIB.setDescription('This APACHE-MIB module contains application specific managed objects for the Apache HTTP-server.')
jointResearchCentre = MibIdentifier((1, 3, 6, 1, 4, 1, 1847))
jrcMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 1847, 1))
class ApacheServerStatusType(TextualConvention, Integer32):
    description = 'The ApacheServerStatusType defines the types for a server.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("dead", 1), ("starting", 2), ("ready", 3), ("read", 4), ("write", 5), ("keepalive", 6), ("log", 7), ("dns", 8), ("graceful", 9))

apacheMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4, 1))
apScoreBoardTable = MibTable((1, 3, 6, 1, 4, 1, 4, 1, 1), )
if mibBuilder.loadTexts: apScoreBoardTable.setStatus('current')
if mibBuilder.loadTexts: apScoreBoardTable.setDescription('This table maintains managed objects for the scoreboard.')
apScoreBoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4, 1, 1, 1), ).setIndexNames((0, "APACHE-MIB", "apScoreBoardIndex"))
if mibBuilder.loadTexts: apScoreBoardEntry.setStatus('current')
if mibBuilder.loadTexts: apScoreBoardEntry.setDescription('The ApScoreBoardEntry.')
apScoreBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: apScoreBoardIndex.setStatus('current')
if mibBuilder.loadTexts: apScoreBoardIndex.setDescription('The scoreboard index of the servers maintained in this running Apache HTTP-server.')
apScoreBoardProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apScoreBoardProcessId.setStatus('current')
if mibBuilder.loadTexts: apScoreBoardProcessId.setDescription('The ProcessID of the server.')
apScoreBoardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 3), ApacheServerStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apScoreBoardStatus.setStatus('current')
if mibBuilder.loadTexts: apScoreBoardStatus.setDescription('The status of the server.')
apScoreBoardStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apScoreBoardStartTime.setStatus('current')
if mibBuilder.loadTexts: apScoreBoardStartTime.setDescription('The timestamp of when this server became active.')
apScoreBoardAccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apScoreBoardAccessCount.setStatus('current')
if mibBuilder.loadTexts: apScoreBoardAccessCount.setDescription('The number of accesses handled by this server.')
apScoreBoardAccessBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apScoreBoardAccessBytes.setStatus('current')
if mibBuilder.loadTexts: apScoreBoardAccessBytes.setDescription('The number of bytes responded by this server.')
apScoreBoardClient = MibTableColumn((1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apScoreBoardClient.setStatus('current')
if mibBuilder.loadTexts: apScoreBoardClient.setDescription('The client that is connected to the server.')
apScoreBoardRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apScoreBoardRequest.setStatus('current')
if mibBuilder.loadTexts: apScoreBoardRequest.setDescription('The request that the client did.')
apScoreBoardVirtualHost = MibTableColumn((1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apScoreBoardVirtualHost.setStatus('current')
if mibBuilder.loadTexts: apScoreBoardVirtualHost.setDescription('The virtual host being access at the server.')
apMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4, 2))
apMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4, 2, 1))
apMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4, 2, 2))
apScoreBoardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4, 2, 2, 1)).setObjects(("APACHE-MIB", "apScoreBoardProcessId"), ("APACHE-MIB", "apScoreBoardStatus"), ("APACHE-MIB", "apScoreBoardStartTime"), ("APACHE-MIB", "apScoreBoardAccessCount"), ("APACHE-MIB", "apScoreBoardAccessBytes"), ("APACHE-MIB", "apScoreBoardClient"), ("APACHE-MIB", "apScoreBoardRequest"), ("APACHE-MIB", "apScoreBoardVirtualHost"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apScoreBoardGroup = apScoreBoardGroup.setStatus('current')
if mibBuilder.loadTexts: apScoreBoardGroup.setDescription('')
mibBuilder.exportSymbols("APACHE-MIB", apScoreBoardVirtualHost=apScoreBoardVirtualHost, apScoreBoardTable=apScoreBoardTable, apScoreBoardRequest=apScoreBoardRequest, apScoreBoardStatus=apScoreBoardStatus, apScoreBoardClient=apScoreBoardClient, apScoreBoardAccessBytes=apScoreBoardAccessBytes, apMIBConformance=apMIBConformance, apMIBCompliances=apMIBCompliances, apScoreBoardGroup=apScoreBoardGroup, jointResearchCentre=jointResearchCentre, ApacheServerStatusType=ApacheServerStatusType, apacheMIB=apacheMIB, apScoreBoardEntry=apScoreBoardEntry, apMIBGroups=apMIBGroups, apacheMIBObjects=apacheMIBObjects, PYSNMP_MODULE_ID=apacheMIB, jrcMIBs=jrcMIBs, apScoreBoardIndex=apScoreBoardIndex, apScoreBoardAccessCount=apScoreBoardAccessCount, apScoreBoardStartTime=apScoreBoardStartTime, apScoreBoardProcessId=apScoreBoardProcessId)
