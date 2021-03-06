#
# PySNMP MIB module PROCESS-DETAILS-SUNMANAGEMENTCENTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PROCESS-DETAILS-SUNMANAGEMENTCENTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:33:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, ObjectIdentity, Counter32, TimeTicks, Counter64, IpAddress, NotificationType, Integer32, enterprises, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "ObjectIdentity", "Counter32", "TimeTicks", "Counter64", "IpAddress", "NotificationType", "Integer32", "enterprises", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
processDetails = ModuleIdentity((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13))
processDetails.setRevisions(('1999-07-20 15:05',))
if mibBuilder.loadTexts: processDetails.setLastUpdated('9907201505Z')
if mibBuilder.loadTexts: processDetails.setOrganization('Sun Microsystems Inc.')
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
prod = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
sunsymon = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12))
agent = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2))
modules = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2))
processTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1), )
if mibBuilder.loadTexts: processTable.setStatus('current')
processTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1), ).setIndexNames((0, "PROCESS-DETAILS-SUNMANAGEMENTCENTER-MIB", "psProcessID"))
if mibBuilder.loadTexts: processTableEntry.setStatus('current')
psProcessID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProcessID.setStatus('current')
psParentProcessID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psParentProcessID.setStatus('current')
psUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psUserID.setStatus('current')
psUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psUserName.setStatus('current')
psEUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEUserID.setStatus('current')
psGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psGroupID.setStatus('current')
psEGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEGroupID.setStatus('current')
psSessionID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psSessionID.setStatus('current')
psProcessGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProcessGroupID.setStatus('current')
psControlTTY = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psControlTTY.setStatus('current')
psStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psStartTime.setStatus('current')
psExecutionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psExecutionTime.setStatus('current')
psState = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psState.setStatus('current')
psWaitChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psWaitChannel.setStatus('current')
psSchedulingClass = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psSchedulingClass.setStatus('current')
psAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psAddress.setStatus('current')
psSize = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psSize.setStatus('current')
psPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPriority.setStatus('current')
psNice = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psNice.setStatus('current')
psPercentCPUTime = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPercentCPUTime.setStatus('current')
psPercentMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPercentMemory.setStatus('current')
psCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psCommand.setStatus('current')
psCommandLine = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psCommandLine.setStatus('current')
psZoneID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13, 1, 1, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psZoneID.setStatus('current')
mibBuilder.exportSymbols("PROCESS-DETAILS-SUNMANAGEMENTCENTER-MIB", psSchedulingClass=psSchedulingClass, psNice=psNice, psSessionID=psSessionID, psEUserID=psEUserID, agent=agent, psParentProcessID=psParentProcessID, psCommandLine=psCommandLine, psAddress=psAddress, psExecutionTime=psExecutionTime, psPercentCPUTime=psPercentCPUTime, psControlTTY=psControlTTY, psState=psState, modules=modules, psUserName=psUserName, psPriority=psPriority, psPercentMemory=psPercentMemory, processDetails=processDetails, prod=prod, PYSNMP_MODULE_ID=processDetails, psWaitChannel=psWaitChannel, psEGroupID=psEGroupID, psGroupID=psGroupID, psSize=psSize, sunsymon=sunsymon, psUserID=psUserID, processTable=processTable, processTableEntry=processTableEntry, psCommand=psCommand, psProcessGroupID=psProcessGroupID, psZoneID=psZoneID, sun=sun, psStartTime=psStartTime, psProcessID=psProcessID)
