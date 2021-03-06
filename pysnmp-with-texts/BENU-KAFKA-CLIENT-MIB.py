#
# PySNMP MIB module BENU-KAFKA-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BENU-KAFKA-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:37:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
benuWAG, = mibBuilder.importSymbols("BENU-WAG-MIB", "benuWAG")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, Bits, Unsigned32, NotificationType, iso, Gauge32, ModuleIdentity, Integer32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Bits", "Unsigned32", "NotificationType", "iso", "Gauge32", "ModuleIdentity", "Integer32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuKafkaClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12))
benuKafkaClientMIB.setRevisions(('2015-10-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: benuKafkaClientMIB.setRevisionsDescriptions(('Initial Version',))
if mibBuilder.loadTexts: benuKafkaClientMIB.setLastUpdated('201510210000Z')
if mibBuilder.loadTexts: benuKafkaClientMIB.setOrganization('Benu Networks,Inc')
if mibBuilder.loadTexts: benuKafkaClientMIB.setContactInfo('Benu Networks,Inc Corporate Headquarters 300 Concord Road, Suite 110 Billerica, MA 01821 USA Tel: +1 978-223-4700 Fax: +1 978-362-1908 Email: info@benunets.com')
if mibBuilder.loadTexts: benuKafkaClientMIB.setDescription('This MIB module defines management information related to the KAFKA client. Copyright (C) 2013 by Benu Networks, Inc. All rights reserved.')
bKafkaClientObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1))
if mibBuilder.loadTexts: bKafkaClientObjects.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientObjects.setDescription('KAFKA client information is defined in this branch.')
bKafkaClientLatencyTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1), )
if mibBuilder.loadTexts: bKafkaClientLatencyTable.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyTable.setDescription('Latency information list for KAFKA client.')
bKafkaClientLatencyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1), ).setIndexNames((0, "BENU-KAFKA-CLIENT-MIB", "bKafkaClientLatencyStatsInterval"))
if mibBuilder.loadTexts: bKafkaClientLatencyEntry.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyEntry.setDescription('A logical row in the bKafkaClientLatencyTable.')
bKafkaClientLatencyStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bKafkaClientLatencyStatsInterval.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyStatsInterval.setDescription('The interval during which the measurements were accumulated. The interval index one indicates the latest interval for which statistics accumulation was completed. Older the statistics data, greater the interval index value. In a system supporting a history of n intervals with IntervalCount(1) and IntervalCount(n), the most and least recent intervals respectively, the following applies at the end of an interval: - discard the value of IntervalCount(n) - the value of IntervalCount(i) becomes that of IntervalCount(i+1) for 1 <= i < n - the value of IntervalCount(1) becomes that of CurrentCount.')
bKafkaClientLatencyStatsIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyStatsIntervalDuration.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyStatsIntervalDuration.setDescription('Kafka client latency stats interval duration.')
bKafkaClientLatencyTotalPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyTotalPktCount.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyTotalPktCount.setDescription('The count of total number of packets handled by Kafka client.')
bKafkaClientLatencyMaxProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyMaxProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyMaxProcessingTime.setDescription('Maximum packet processing time handled by Kafka client in micro seconds.')
bKafkaClientLatencyMinProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyMinProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyMinProcessingTime.setDescription('Minimum packet processing time handled by Kafka client in micro seconds.')
bKafkaClientLatencyAvgProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyAvgProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyAvgProcessingTime.setDescription('Average packet processing time handled by Kafka client in micro seconds.')
bKafkaClientLatencyProcessTimeMorethan1MSPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyProcessTimeMorethan1MSPktCount.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyProcessTimeMorethan1MSPktCount.setDescription('Number of packets took more than 1 milli second processing time handled by Kafka client.')
mibBuilder.exportSymbols("BENU-KAFKA-CLIENT-MIB", PYSNMP_MODULE_ID=benuKafkaClientMIB, bKafkaClientLatencyAvgProcessingTime=bKafkaClientLatencyAvgProcessingTime, bKafkaClientLatencyEntry=bKafkaClientLatencyEntry, bKafkaClientObjects=bKafkaClientObjects, bKafkaClientLatencyMinProcessingTime=bKafkaClientLatencyMinProcessingTime, bKafkaClientLatencyMaxProcessingTime=bKafkaClientLatencyMaxProcessingTime, bKafkaClientLatencyStatsInterval=bKafkaClientLatencyStatsInterval, bKafkaClientLatencyProcessTimeMorethan1MSPktCount=bKafkaClientLatencyProcessTimeMorethan1MSPktCount, benuKafkaClientMIB=benuKafkaClientMIB, bKafkaClientLatencyTable=bKafkaClientLatencyTable, bKafkaClientLatencyStatsIntervalDuration=bKafkaClientLatencyStatsIntervalDuration, bKafkaClientLatencyTotalPktCount=bKafkaClientLatencyTotalPktCount)
