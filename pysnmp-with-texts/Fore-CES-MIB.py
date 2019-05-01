#
# PySNMP MIB module Fore-CES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-CES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:16:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
asxd, = mibBuilder.importSymbols("Fore-Common-MIB", "asxd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, Counter64, ObjectIdentity, Counter32, IpAddress, TimeTicks, NotificationType, Bits, Integer32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Counter64", "ObjectIdentity", "Counter32", "IpAddress", "TimeTicks", "NotificationType", "Bits", "Integer32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, TimeInterval, TestAndIncr, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeInterval", "TestAndIncr", "DisplayString")
cesExtGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16))
if mibBuilder.loadTexts: cesExtGroup.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: cesExtGroup.setOrganization('FORE')
if mibBuilder.loadTexts: cesExtGroup.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: cesExtGroup.setDescription('Fore Systems CES MIB Definitions')
cesExtTable = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 1), TestAndIncr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cesExtTable.setStatus('current')
if mibBuilder.loadTexts: cesExtTable.setDescription('This indicates the value of the next available index to be used for CES creation')
cbrctConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2), )
if mibBuilder.loadTexts: cbrctConfTable.setStatus('current')
if mibBuilder.loadTexts: cbrctConfTable.setDescription('A table of CBR Cut-through configuration information.')
cbrctConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cbrctConfEntry.setStatus('current')
if mibBuilder.loadTexts: cbrctConfEntry.setDescription('A table entry containing CBR Cut-through configuration information for each CES connection. ')
cbrctState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cbrctState.setStatus('current')
if mibBuilder.loadTexts: cbrctState.setDescription('This variable indicates whether the CBR Cut-through feature is enabled or disabled on the ingress connection . The values mean: enabled CBR Cut-through enabled disabled CBR Cut-through disabled')
cbrctIdleDetection = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idlePattern", 1), ("cas", 2))).clone('idlePattern')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cbrctIdleDetection.setStatus('current')
if mibBuilder.loadTexts: cbrctIdleDetection.setDescription('This variable identifies the idle detection mechanism used on this connection. The different values are: idlePattern(1) detection is based on idle pattern detection cas(2) detection is based on CAS signalling')
cbrctIdleMask = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 3), Integer32().clone(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cbrctIdleMask.setStatus('current')
if mibBuilder.loadTexts: cbrctIdleMask.setDescription('This contains the mask pattern for idle detection.')
cbrctNoOfIdlePatterns = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 4), Integer32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cbrctNoOfIdlePatterns.setStatus('current')
if mibBuilder.loadTexts: cbrctNoOfIdlePatterns.setDescription('This variable contains the number of idle patterns configured for detection.')
cbrctIdlePatterns = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 5), Integer32().clone(32767)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cbrctIdlePatterns.setStatus('current')
if mibBuilder.loadTexts: cbrctIdlePatterns.setDescription('This contains the patterns for idle detection. For detection based on both idle and mask patterns it contains the idle octet patterns. For detection based on signalling it contains the octet value of AB signalling bits (eg. 00000010 (02H), the bit 0 is B bit and bit 1 is A bit). Maximum of 4 idle patter ns are used. The idle patterns get filled from the least significant byte. The cbrctNoOfIdlePatterns gives the number of idle patterns.')
cbrctIdleIntPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 6), TimeInterval().clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cbrctIdleIntPeriod.setStatus('current')
if mibBuilder.loadTexts: cbrctIdleIntPeriod.setDescription('This contains the integration period for idle detection.')
cbrctActiveIntPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 7), TimeInterval().clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cbrctActiveIntPeriod.setStatus('current')
if mibBuilder.loadTexts: cbrctActiveIntPeriod.setDescription('This contains the integration period for active detection.')
mibBuilder.exportSymbols("Fore-CES-MIB", cbrctState=cbrctState, cbrctIdleDetection=cbrctIdleDetection, cbrctNoOfIdlePatterns=cbrctNoOfIdlePatterns, cbrctIdlePatterns=cbrctIdlePatterns, cbrctActiveIntPeriod=cbrctActiveIntPeriod, cbrctIdleMask=cbrctIdleMask, cbrctIdleIntPeriod=cbrctIdleIntPeriod, cesExtTable=cesExtTable, cbrctConfTable=cbrctConfTable, cesExtGroup=cesExtGroup, PYSNMP_MODULE_ID=cesExtGroup, cbrctConfEntry=cbrctConfEntry)
