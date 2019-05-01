#
# PySNMP MIB module IPFIX-COLLECTOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPFIX-COLLECTOR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:55:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, iso, Bits, Unsigned32, MibIdentifier, Integer32, Counter64, mib_2, IpAddress, TimeTicks, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "iso", "Bits", "Unsigned32", "MibIdentifier", "Integer32", "Counter64", "mib-2", "IpAddress", "TimeTicks", "ObjectIdentity", "NotificationType")
RowStatus, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "DisplayString")
ipfixMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 999))
ipfixMIB.setRevisions(('2006-10-20 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipfixMIB.setRevisionsDescriptions(('Initial version, published as RFC yyyy.',))
if mibBuilder.loadTexts: ipfixMIB.setLastUpdated('200610201600Z')
if mibBuilder.loadTexts: ipfixMIB.setOrganization('IETF IPFIX Working Group')
if mibBuilder.loadTexts: ipfixMIB.setContactInfo('WG charter: http://www.ietf.org/html.charters/ipfix-charter.html Mailing Lists: General Discussion: ipfix@ietf.org To Subscribe: majordomo@net.doit.wisc.edu In Body: subscribe ipfix Archive: http://ipfix.doit.wisc.edu/archive/ Editor: Atsushi Kobayashi NTT Information Sharing Platform Laboratories 3-9-11 Midori-cho Musashino-shi 180-8585 Japan Phone: +81-422-59-3978 Email: akoba@nttv6.net')
if mibBuilder.loadTexts: ipfixMIB.setDescription("The IPFIX collector MIB defines managed objects that are maintained by the collecting process in traffic collector or IPFIX concentrator. These objects provide informations that are exporter's profile data and received templates. Exporter's profile has that exporter's ip address and port number. In addition, these object has statistics data per session or per templates. Copyright (C) The Internet Society (2005). This version of this MIB module is part of RFC yyyy; see the RFC itself for full legal notices.")
ipfixExporter = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1))
ipfixCollector = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 2))
ipfixPsampExtension = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 3))
ipfixConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 4))
ipfixCollectorObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 2, 1))
ipfixCollectorConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 2, 2))
ipfixReceiving = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 2, 1, 1))
ipfixExporterTable = MibTable((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 1), )
if mibBuilder.loadTexts: ipfixExporterTable.setStatus('current')
if mibBuilder.loadTexts: ipfixExporterTable.setDescription('This table lists Exporters that received by collecting process. This process manages them.')
ipfixExporterEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 1, 1), ).setIndexNames((0, "IPFIX-COLLECTOR-MIB", "ipfixExporterIndex"))
if mibBuilder.loadTexts: ipfixExporterEntry.setStatus('current')
if mibBuilder.loadTexts: ipfixExporterEntry.setDescription('Defines an entry in the ipfixExporterTable')
ipfixExporterIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipfixExporterIndex.setStatus('current')
if mibBuilder.loadTexts: ipfixExporterIndex.setDescription("Locally arbitrary, but unique identifier of an entry in ipfixExporterTable. The value is expected to remain constant from a re-initialization of the entity's network management system to the next re-initialization.")
ipfixExporterIpAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixExporterIpAddressType.setStatus('current')
if mibBuilder.loadTexts: ipfixExporterIpAddressType.setDescription('The IP address type of the exporter. The value for IPv4 is ipv4(1). The value for IPv6 is ipv6(2).')
ipfixExporterIpAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixExporterIpAddress.setStatus('current')
if mibBuilder.loadTexts: ipfixExporterIpAddress.setDescription('The IP address of the Exporter.')
ipfixLifeTimeTemplate = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixLifeTimeTemplate.setStatus('current')
if mibBuilder.loadTexts: ipfixLifeTimeTemplate.setDescription('This is the time interval in seconds for the Life Time configured for the template with this session. It is only used to manage the received templates, if this protocol is UDP. The collecting process discards the template, if the templates is not refreshed within this life time.')
ipfixSessionTable = MibTable((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2), )
if mibBuilder.loadTexts: ipfixSessionTable.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionTable.setDescription('This table lists sessions between exporting process and collecting process. This table has now, or has at some time in the past, established session.')
ipfixSessionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2, 1), ).setIndexNames((0, "IPFIX-COLLECTOR-MIB", "ipfixExporterIndex"), (0, "IPFIX-COLLECTOR-MIB", "ipfixSessionId"))
if mibBuilder.loadTexts: ipfixSessionEntry.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionEntry.setDescription('Defines an entry in the ipfixSessionTable')
ipfixSessionId = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipfixSessionId.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionId.setDescription("Locally arbitrary, but unique identifier of an entry in ipfixSessionTable. The value is expected to remain constant from a re-initialization of the entity's network management system to the next re-initialization.")
ipfixSessionStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixSessionStatus.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionStatus.setDescription('The status of this session.')
ipfixSessionProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixSessionProtocol.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionProtocol.setDescription('The transport protocol is used for receiving sampled packets from the Exporter. The recommended protocols are TCP (6), UDP (17) and SCTP (132). The default is SCTP.')
ipfixSessionDstPort = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixSessionDstPort.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionDstPort.setDescription('The transport protocol port number of exporter which enables exporting process.')
ipfixSessionSrcPort = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixSessionSrcPort.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionSrcPort.setDescription('The transport protocol port number of self device which enables collecting Process.')
ipfixSessionStatsTable = MibTable((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3), )
if mibBuilder.loadTexts: ipfixSessionStatsTable.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionStatsTable.setDescription('This table lists sessions statistics between exporting process and collecting process. The collecting process manages them.')
ipfixSessionStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3, 1), ).setIndexNames((0, "IPFIX-COLLECTOR-MIB", "ipfixExporterIndex"), (0, "IPFIX-COLLECTOR-MIB", "ipfixSessionId"))
if mibBuilder.loadTexts: ipfixSessionStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionStatsEntry.setDescription('Defines an entry in the ipfixSessionStatsTable')
ipfixSessionPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixSessionPackets.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionPackets.setDescription('The number of packets received from the Exporter through this session.')
ipfixSessionBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixSessionBytes.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionBytes.setDescription('The number of bytes received from the exporter through this session.')
ipfixSessionMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixSessionMessages.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionMessages.setDescription('The number of IPFIX messages received from the exporter through this session.')
ipfixSessionDiscardMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixSessionDiscardMessages.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionDiscardMessages.setDescription('This indicates the number of received IPFIX Message that might be malformed or cant not be encoded.')
ipfixSessionElapsedTime = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixSessionElapsedTime.setStatus('current')
if mibBuilder.loadTexts: ipfixSessionElapsedTime.setDescription('This timer indicates how long this session has been connected. This elapsed time of the session of IPFIX presents in second.')
ipfixObdomainStatsTable = MibTable((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4), )
if mibBuilder.loadTexts: ipfixObdomainStatsTable.setStatus('current')
if mibBuilder.loadTexts: ipfixObdomainStatsTable.setDescription('This table lists statistics objects that have data per observation domain.')
ipfixObdomainStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1), ).setIndexNames((0, "IPFIX-COLLECTOR-MIB", "ipfixExporterIndex"), (0, "IPFIX-COLLECTOR-MIB", "ipfixSessionId"), (0, "IPFIX-COLLECTOR-MIB", "ipfixObdomainId"))
if mibBuilder.loadTexts: ipfixObdomainStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ipfixObdomainStatsEntry.setDescription('Defines an entry in the ipfixObdomainStatsTable.')
ipfixObdomainId = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipfixObdomainId.setStatus('current')
if mibBuilder.loadTexts: ipfixObdomainId.setDescription('It uses the observation domain id in the received IPFIX message header.')
ipfixObdomainMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixObdomainMessages.setStatus('current')
if mibBuilder.loadTexts: ipfixObdomainMessages.setDescription('The number of IPFIX messages received from the Exporter.')
ipfixObdomainFlows = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixObdomainFlows.setStatus('current')
if mibBuilder.loadTexts: ipfixObdomainFlows.setDescription('The number of flow records received from the Exporter.')
ipfixObdomainTemplates = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixObdomainTemplates.setStatus('current')
if mibBuilder.loadTexts: ipfixObdomainTemplates.setDescription('The number of templates received from the Exporter.')
ipfixObdomainLatestSeqNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixObdomainLatestSeqNumber.setStatus('current')
if mibBuilder.loadTexts: ipfixObdomainLatestSeqNumber.setDescription('The latest sequence number. The collecting process overwrites to this object when it receives IPFIX message.')
ipfixObdomainDisorderdSeqNumbers = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixObdomainDisorderdSeqNumbers.setStatus('current')
if mibBuilder.loadTexts: ipfixObdomainDisorderdSeqNumbers.setDescription('This counter indicates inconformable numbers of sequence number. The collecting process check consistency between received sequence number and received data flows. This counter is added up this inclement, if it recognize there are some flows that have not been received.')
ipfixTemplateTable = MibTable((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 5), )
if mibBuilder.loadTexts: ipfixTemplateTable.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateTable.setDescription('This table lists templates that are received by the collecting process. This process manages them.')
ipfixTemplateEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 5, 1), ).setIndexNames((0, "IPFIX-COLLECTOR-MIB", "ipfixExporterIndex"), (0, "IPFIX-COLLECTOR-MIB", "ipfixSessionId"), (0, "IPFIX-COLLECTOR-MIB", "ipfixTemplateId"), (0, "IPFIX-COLLECTOR-MIB", "ipfixTemplateIndex"))
if mibBuilder.loadTexts: ipfixTemplateEntry.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateEntry.setDescription('Defines an entry in the ipfixTemplateTable')
ipfixTemplateId = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipfixTemplateId.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateId.setDescription('This number indicates the template id in the IPFIX message.')
ipfixTemplateIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipfixTemplateIndex.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateIndex.setDescription('The ipfixTemplateIndex specifies the order in which the information element ids are used in the template record.')
ipfixTemplateFieldId = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixTemplateFieldId.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateFieldId.setDescription('This indicates the Information Element Id at position ipfixTemplateIndex in the template ipfixTemplateId. This implicitly gives the data type and state values that are received.')
ipfixTemplateFieldLength = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixTemplateFieldLength.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateFieldLength.setDescription('This indicates the length of each Information Element Ids. Especially, in variable length type it is specified as 65535.')
ipfixTemplateStatsTable = MibTable((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 6), )
if mibBuilder.loadTexts: ipfixTemplateStatsTable.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateStatsTable.setDescription('This table lists statistics objects that have data per template.')
ipfixTemplateStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 6, 1), ).setIndexNames((0, "IPFIX-COLLECTOR-MIB", "ipfixExporterIndex"), (0, "IPFIX-COLLECTOR-MIB", "ipfixSessionId"), (0, "IPFIX-COLLECTOR-MIB", "ipfixTemplateId"))
if mibBuilder.loadTexts: ipfixTemplateStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateStatsEntry.setDescription('Defines an entry in the ipfixTemplateStatsTable')
ipfixTempFlows = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixTempFlows.setStatus('current')
if mibBuilder.loadTexts: ipfixTempFlows.setDescription('The number of flow records per template received from Exporter.')
ipfixTempReceivedTime = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 6, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixTempReceivedTime.setStatus('current')
if mibBuilder.loadTexts: ipfixTempReceivedTime.setDescription('Time that the collecting process received this template. The collecting process overwrites to this object when it receives same template.')
ipfixCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 4, 1))
ipfixGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 4, 2))
ipfixCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 999, 4, 1, 1)).setObjects(("IPFIX-COLLECTOR-MIB", "ipfixGroupExporters"), ("IPFIX-COLLECTOR-MIB", "ipfixGroupTemplates"), ("IPFIX-COLLECTOR-MIB", "ipfixGroupStatistics"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixCompliance = ipfixCompliance.setStatus('current')
if mibBuilder.loadTexts: ipfixCompliance.setDescription('An implementation that complies to this module must implement the objects defined in the mandatory groups collectGroupExporters, collectGroupTemplates. The imeplementation of all other objects depends on the imeplementation of the corresponding functionality in the equipment.')
ipfixGroupExporters = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 4, 2, 1)).setObjects(("IPFIX-COLLECTOR-MIB", "ipfixExporterIpAddressType"), ("IPFIX-COLLECTOR-MIB", "ipfixExporterIpAddress"), ("IPFIX-COLLECTOR-MIB", "ipfixLifeTimeTemplate"), ("IPFIX-COLLECTOR-MIB", "ipfixSessionProtocol"), ("IPFIX-COLLECTOR-MIB", "ipfixSessionDstPort"), ("IPFIX-COLLECTOR-MIB", "ipfixSessionSrcPort"), ("IPFIX-COLLECTOR-MIB", "ipfixSessionStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixGroupExporters = ipfixGroupExporters.setStatus('current')
if mibBuilder.loadTexts: ipfixGroupExporters.setDescription('All objects that are basic for the management function of exporters.')
ipfixGroupTemplates = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 4, 2, 2)).setObjects(("IPFIX-COLLECTOR-MIB", "ipfixTemplateFieldId"), ("IPFIX-COLLECTOR-MIB", "ipfixTemplateFieldLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixGroupTemplates = ipfixGroupTemplates.setStatus('current')
if mibBuilder.loadTexts: ipfixGroupTemplates.setDescription('All objects that are basic for the management function of templates.')
ipfixGroupStatistics = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 4, 2, 3)).setObjects(("IPFIX-COLLECTOR-MIB", "ipfixSessionPackets"), ("IPFIX-COLLECTOR-MIB", "ipfixSessionBytes"), ("IPFIX-COLLECTOR-MIB", "ipfixSessionMessages"), ("IPFIX-COLLECTOR-MIB", "ipfixSessionDiscardMessages"), ("IPFIX-COLLECTOR-MIB", "ipfixSessionElapsedTime"), ("IPFIX-COLLECTOR-MIB", "ipfixObdomainMessages"), ("IPFIX-COLLECTOR-MIB", "ipfixObdomainFlows"), ("IPFIX-COLLECTOR-MIB", "ipfixObdomainTemplates"), ("IPFIX-COLLECTOR-MIB", "ipfixObdomainLatestSeqNumber"), ("IPFIX-COLLECTOR-MIB", "ipfixObdomainDisorderdSeqNumbers"), ("IPFIX-COLLECTOR-MIB", "ipfixTempFlows"), ("IPFIX-COLLECTOR-MIB", "ipfixTempReceivedTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixGroupStatistics = ipfixGroupStatistics.setStatus('current')
if mibBuilder.loadTexts: ipfixGroupStatistics.setDescription('All objects that are basic for the statistics function.')
mibBuilder.exportSymbols("IPFIX-COLLECTOR-MIB", ipfixCollectorConformance=ipfixCollectorConformance, ipfixTemplateEntry=ipfixTemplateEntry, ipfixLifeTimeTemplate=ipfixLifeTimeTemplate, ipfixSessionMessages=ipfixSessionMessages, ipfixTempFlows=ipfixTempFlows, ipfixSessionEntry=ipfixSessionEntry, ipfixObdomainFlows=ipfixObdomainFlows, ipfixSessionSrcPort=ipfixSessionSrcPort, ipfixObdomainTemplates=ipfixObdomainTemplates, ipfixSessionDstPort=ipfixSessionDstPort, ipfixReceiving=ipfixReceiving, ipfixCompliances=ipfixCompliances, ipfixGroupStatistics=ipfixGroupStatistics, ipfixExporterIndex=ipfixExporterIndex, ipfixExporterIpAddressType=ipfixExporterIpAddressType, ipfixGroupExporters=ipfixGroupExporters, ipfixTempReceivedTime=ipfixTempReceivedTime, ipfixSessionTable=ipfixSessionTable, ipfixSessionId=ipfixSessionId, ipfixMIB=ipfixMIB, ipfixObdomainStatsTable=ipfixObdomainStatsTable, ipfixTemplateFieldLength=ipfixTemplateFieldLength, ipfixTemplateIndex=ipfixTemplateIndex, ipfixExporterEntry=ipfixExporterEntry, ipfixCompliance=ipfixCompliance, ipfixGroups=ipfixGroups, ipfixSessionStatsTable=ipfixSessionStatsTable, ipfixSessionElapsedTime=ipfixSessionElapsedTime, ipfixCollectorObjects=ipfixCollectorObjects, ipfixSessionBytes=ipfixSessionBytes, ipfixSessionStatus=ipfixSessionStatus, ipfixTemplateTable=ipfixTemplateTable, ipfixExporterIpAddress=ipfixExporterIpAddress, ipfixSessionPackets=ipfixSessionPackets, ipfixExporter=ipfixExporter, ipfixObdomainMessages=ipfixObdomainMessages, PYSNMP_MODULE_ID=ipfixMIB, ipfixTemplateStatsEntry=ipfixTemplateStatsEntry, ipfixSessionDiscardMessages=ipfixSessionDiscardMessages, ipfixObdomainId=ipfixObdomainId, ipfixGroupTemplates=ipfixGroupTemplates, ipfixConformance=ipfixConformance, ipfixTemplateFieldId=ipfixTemplateFieldId, ipfixCollector=ipfixCollector, ipfixSessionStatsEntry=ipfixSessionStatsEntry, ipfixObdomainLatestSeqNumber=ipfixObdomainLatestSeqNumber, ipfixTemplateId=ipfixTemplateId, ipfixTemplateStatsTable=ipfixTemplateStatsTable, ipfixPsampExtension=ipfixPsampExtension, ipfixObdomainStatsEntry=ipfixObdomainStatsEntry, ipfixSessionProtocol=ipfixSessionProtocol, ipfixExporterTable=ipfixExporterTable, ipfixObdomainDisorderdSeqNumbers=ipfixObdomainDisorderdSeqNumbers)
