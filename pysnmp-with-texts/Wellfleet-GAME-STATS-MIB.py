#
# PySNMP MIB module Wellfleet-GAME-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-GAME-STATS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter64, ObjectIdentity, Unsigned32, MibIdentifier, IpAddress, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, ModuleIdentity, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "ObjectIdentity", "Unsigned32", "MibIdentifier", "IpAddress", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "ModuleIdentity", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfGameGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfGameGroup")
wfKernelTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1), )
if mibBuilder.loadTexts: wfKernelTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelTable.setDescription('Table of kernel statistics, indexed by slot number')
wfKernelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1), ).setIndexNames((0, "Wellfleet-GAME-STATS-MIB", "wfKernelSlot"))
if mibBuilder.loadTexts: wfKernelEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelEntry.setDescription('A particular interface')
wfKernelSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelSlot.setDescription('The slot number indexes the kernel statistics table')
wfKernelMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemorySize.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemorySize.setDescription('The total size of allocatable memory, in bytes')
wfKernelMemoryFree = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemoryFree.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemoryFree.setDescription("The amount of memory which hasn't been allocated yet, in bytes")
wfKernelMemorySegsTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemorySegsTotal.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemorySegsTotal.setDescription('Total number of memory segments in the kernel')
wfKernelMemorySegsFree = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemorySegsFree.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemorySegsFree.setDescription('Total number of unallocated memory segments in the kernel')
wfKernelMemoryMaxSegFree = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemoryMaxSegFree.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemoryMaxSegFree.setDescription('Size of the largest unallocated memory segment')
wfKernelBuffersTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBuffersTotal.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBuffersTotal.setDescription('Total number of packet buffers')
wfKernelBuffersFree = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBuffersFree.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBuffersFree.setDescription('Number of packet buffers in the free pool')
wfKernelTasksTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelTasksTotal.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelTasksTotal.setDescription('Number of tasks running')
wfKernelTasksInQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelTasksInQueue.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelTasksInQueue.setDescription('Number of tasks awaiting scheduling')
wfKernelTimersTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelTimersTotal.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelTimersTotal.setDescription('Total number of timers available')
wfKernelTimersActive = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelTimersActive.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelTimersActive.setDescription('Total number of timers in use by tasks')
wfKernelBufOwnerTask1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask1.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask1.setDescription('Activation address of task which owns many buffers')
wfKernelBufOwnerTask1Bufs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask1Bufs.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask1Bufs.setDescription('Number of buffers owned by the task')
wfKernelBufOwnerTask2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask2.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask2.setDescription('Activation address of task which owns many buffers')
wfKernelBufOwnerTask2Bufs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask2Bufs.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask2Bufs.setDescription('Number of buffers owned by the task')
wfKernelBufOwnerTask3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask3.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask3.setDescription('Activation address of task which owns many buffers')
wfKernelBufOwnerTask3Bufs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask3Bufs.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask3Bufs.setDescription('Number of buffers owned by the task')
wfKernelBufOwnerTask4 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask4.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask4.setDescription('Activation address of task which owns many buffers')
wfKernelBufOwnerTask4Bufs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask4Bufs.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask4Bufs.setDescription('Number of buffers owned by the task')
wfKernelBufOwnerTask5 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask5.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask5.setDescription('Activation address of task which owns many buffers')
wfKernelBufOwnerTask5Bufs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask5Bufs.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask5Bufs.setDescription('Number of buffers owned by the task')
wfKernelBufOwnerTask6 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask6.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask6.setDescription('Activation address of task which owns many buffers')
wfKernelBufOwnerTask6Bufs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask6Bufs.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask6Bufs.setDescription('Number of buffers owned by the task')
wfKernelBufOwnerTask7 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask7.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask7.setDescription('Activation address of task which owns many buffers')
wfKernelBufOwnerTask7Bufs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask7Bufs.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask7Bufs.setDescription('Number of buffers owned by the task')
wfKernelBufOwnerTask8 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 27), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask8.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask8.setDescription('Activation address of task which owns many buffers')
wfKernelBufOwnerTask8Bufs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask8Bufs.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask8Bufs.setDescription('Number of buffers owned by the task')
wfKernelBufOwnerTask9 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 29), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask9.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask9.setDescription('Activation address of task which owns many buffers')
wfKernelBufOwnerTask9Bufs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask9Bufs.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask9Bufs.setDescription('Number of buffers owned by the task')
wfKernelBufOwnerTask10 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 31), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask10.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask10.setDescription('Activation address of task which owns many buffers')
wfKernelBufOwnerTask10Bufs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBufOwnerTask10Bufs.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBufOwnerTask10Bufs.setDescription('Number of buffers owned by the task')
wfKernelMemOwnerTask1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 33), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask1.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask1.setDescription('Activation address of task which owns a sizable amount of memory')
wfKernelMemOwnerTask1Size = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask1Size.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask1Size.setDescription('Amount of memory owned by the task')
wfKernelMemOwnerTask2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 35), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask2.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask2.setDescription('Activation address of task which owns a sizable amount of memory')
wfKernelMemOwnerTask2Size = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask2Size.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask2Size.setDescription('Amount of memory owned by the task')
wfKernelMemOwnerTask3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 37), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask3.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask3.setDescription('Activation address of task which owns a sizable amount of memory')
wfKernelMemOwnerTask3Size = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 38), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask3Size.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask3Size.setDescription('Amount of memory owned by the task')
wfKernelMemOwnerTask4 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 39), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask4.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask4.setDescription('Activation address of task which owns a sizable amount of memory')
wfKernelMemOwnerTask4Size = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 40), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask4Size.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask4Size.setDescription('Amount of memory owned by the task')
wfKernelMemOwnerTask5 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 41), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask5.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask5.setDescription('Activation address of task which owns a sizable amount of memory')
wfKernelMemOwnerTask5Size = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 42), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask5Size.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask5Size.setDescription('Amount of memory owned by the task')
wfKernelMemOwnerTask6 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 43), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask6.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask6.setDescription('Activation address of task which owns a sizable amount of memory')
wfKernelMemOwnerTask6Size = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 44), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask6Size.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask6Size.setDescription('Amount of memory owned by the task')
wfKernelMemOwnerTask7 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 45), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask7.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask7.setDescription('Activation address of task which owns a sizable amount of memory')
wfKernelMemOwnerTask7Size = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 46), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask7Size.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask7Size.setDescription('Amount of memory owned by the task')
wfKernelMemOwnerTask8 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 47), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask8.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask8.setDescription('Activation address of task which owns a sizable amount of memory')
wfKernelMemOwnerTask8Size = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 48), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask8Size.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask8Size.setDescription('Amount of memory owned by the task')
wfKernelMemOwnerTask9 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 49), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask9.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask9.setDescription('Activation address of task which owns a sizable amount of memory')
wfKernelMemOwnerTask9Size = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 50), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask9Size.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask9Size.setDescription('Amount of memory owned by the task')
wfKernelMemOwnerTask10 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 51), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask10.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask10.setDescription('Activation address of task which owns a sizable amount of memory')
wfKernelMemOwnerTask10Size = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 52), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemOwnerTask10Size.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemOwnerTask10Size.setDescription('Amount of memory owned by the task')
wfKernelAliasBuffsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 53), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelAliasBuffsDropped.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelAliasBuffsDropped.setDescription('Number of alias buffers dropped due to lack of copy buffers')
wfKernelBallocFail = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 54), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelBallocFail.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelBallocFail.setDescription("The number of times a buffer couldn't be allocated via g_balloc because the free buffer pool was empty")
wfKernelReplenEmpty = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 55), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelReplenEmpty.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelReplenEmpty.setDescription('The number of times the free buffer pool was emptied via g_breplen')
wfKernelMemoryFreeLow = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelMemoryFreeLow.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelMemoryFreeLow.setDescription('The low point of the free memory pool, in bytes')
wfKernelAliasNoMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelAliasNoMembers.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelAliasNoMembers.setDescription('Number of alias buffers dropped due to either no members, or GID_GAME is the only member')
wfKernParamTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 2), )
if mibBuilder.loadTexts: wfKernParamTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernParamTable.setDescription('Table of kernel parameter records, indexed by slot number')
wfKernParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 2, 1), ).setIndexNames((0, "Wellfleet-GAME-STATS-MIB", "wfKernParamSlot"))
if mibBuilder.loadTexts: wfKernParamEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernParamEntry.setDescription('A particular interface')
wfKernParamSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernParamSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernParamSlot.setDescription('The slot number indexes the kernel parameter table')
wfKernParamTotMem = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernParamTotMem.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernParamTotMem.setDescription('The size of total Physical memory in Kbytes')
wfKernParamLocMem = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernParamLocMem.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernParamLocMem.setDescription('The size of Local memory in Kbytes')
wfKernParamGlobMem = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernParamGlobMem.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernParamGlobMem.setDescription('The size of Global memory in Kbytes')
wfKernCfgParamTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3), )
if mibBuilder.loadTexts: wfKernCfgParamTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernCfgParamTable.setDescription('Table of kernel configurable parameter records, indexed by slot number')
wfKernCfgParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1), ).setIndexNames((0, "Wellfleet-GAME-STATS-MIB", "wfKernCfgParamSlot"))
if mibBuilder.loadTexts: wfKernCfgParamEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernCfgParamEntry.setDescription('A particular interface')
wfKernCfgParamDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfKernCfgParamDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernCfgParamDelete.setDescription('Create/Delete a kernel configurable parameter record.')
wfKernCfgParamSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernCfgParamSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernCfgParamSlot.setDescription('The slot number indexes the kernel configurable parameters record')
wfKernCfgParamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernCfgParamStatus.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernCfgParamStatus.setDescription('Status of last kernel configurable parameter change request.')
wfKernCfgParamLocMem = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernCfgParamLocMem.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernCfgParamLocMem.setDescription('The amount of configured local memory in Kbytes')
wfKernCfgParamGlobMem = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfKernCfgParamGlobMem.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernCfgParamGlobMem.setDescription('The amount of configured global memory in kbytes')
wfKernCfgParamGlobMemReset = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfKernCfgParamGlobMemReset.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernCfgParamGlobMemReset.setDescription('Reset the slot back to the software default global memory size. The software default value for global memory allocation will now be used on this slot for all memory configurations.')
wfKernCfgParamBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfKernCfgParamBufSize.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernCfgParamBufSize.setDescription('The configured buffer size in kbytes ')
wfKernCfgParamBufSizeReset = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfKernCfgParamBufSizeReset.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernCfgParamBufSizeReset.setDescription('Reset the slot back to the software default buffer size. The software default value for buffer size allocation will now be used on this slot for all buffer carvings.')
wfKernelSysCfgTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 5), )
if mibBuilder.loadTexts: wfKernelSysCfgTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelSysCfgTable.setDescription("Table of kernel's system configuration records, indexed by slot number")
wfKernelSysCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 5, 1), ).setIndexNames((0, "Wellfleet-GAME-STATS-MIB", "wfKernelSysCfgSlot"))
if mibBuilder.loadTexts: wfKernelSysCfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelSysCfgEntry.setDescription('A particular interface')
wfKernelSysCfgDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfKernelSysCfgDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelSysCfgDelete.setDescription('Create/Delete a kernel configurable parameter record.')
wfKernelSysCfgSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfKernelSysCfgSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelSysCfgSlot.setDescription("The slot number indexes the kernel's system configuration record")
wfKernelSysCfgLogging = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfKernelSysCfgLogging.setStatus('mandatory')
if mibBuilder.loadTexts: wfKernelSysCfgLogging.setDescription('Status of last kernel configurable parameter change request.')
mibBuilder.exportSymbols("Wellfleet-GAME-STATS-MIB", wfKernelBallocFail=wfKernelBallocFail, wfKernelMemoryFree=wfKernelMemoryFree, wfKernelAliasNoMembers=wfKernelAliasNoMembers, wfKernelTasksTotal=wfKernelTasksTotal, wfKernelBufOwnerTask4Bufs=wfKernelBufOwnerTask4Bufs, wfKernelMemOwnerTask10=wfKernelMemOwnerTask10, wfKernCfgParamTable=wfKernCfgParamTable, wfKernelTasksInQueue=wfKernelTasksInQueue, wfKernelBuffersTotal=wfKernelBuffersTotal, wfKernelBufOwnerTask10=wfKernelBufOwnerTask10, wfKernParamSlot=wfKernParamSlot, wfKernCfgParamSlot=wfKernCfgParamSlot, wfKernCfgParamStatus=wfKernCfgParamStatus, wfKernelMemOwnerTask1Size=wfKernelMemOwnerTask1Size, wfKernelTimersActive=wfKernelTimersActive, wfKernelBufOwnerTask1Bufs=wfKernelBufOwnerTask1Bufs, wfKernParamEntry=wfKernParamEntry, wfKernelMemoryFreeLow=wfKernelMemoryFreeLow, wfKernelMemOwnerTask1=wfKernelMemOwnerTask1, wfKernelBufOwnerTask7Bufs=wfKernelBufOwnerTask7Bufs, wfKernelMemOwnerTask10Size=wfKernelMemOwnerTask10Size, wfKernelSysCfgDelete=wfKernelSysCfgDelete, wfKernelMemOwnerTask8=wfKernelMemOwnerTask8, wfKernelEntry=wfKernelEntry, wfKernelBufOwnerTask6Bufs=wfKernelBufOwnerTask6Bufs, wfKernelMemOwnerTask3=wfKernelMemOwnerTask3, wfKernelMemOwnerTask7Size=wfKernelMemOwnerTask7Size, wfKernelSysCfgTable=wfKernelSysCfgTable, wfKernelAliasBuffsDropped=wfKernelAliasBuffsDropped, wfKernelMemOwnerTask6=wfKernelMemOwnerTask6, wfKernelSlot=wfKernelSlot, wfKernelMemOwnerTask9=wfKernelMemOwnerTask9, wfKernelBufOwnerTask3=wfKernelBufOwnerTask3, wfKernelBufOwnerTask5Bufs=wfKernelBufOwnerTask5Bufs, wfKernCfgParamGlobMem=wfKernCfgParamGlobMem, wfKernelMemOwnerTask4Size=wfKernelMemOwnerTask4Size, wfKernelBufOwnerTask9=wfKernelBufOwnerTask9, wfKernParamTotMem=wfKernParamTotMem, wfKernelBufOwnerTask9Bufs=wfKernelBufOwnerTask9Bufs, wfKernelMemOwnerTask8Size=wfKernelMemOwnerTask8Size, wfKernParamTable=wfKernParamTable, wfKernelTimersTotal=wfKernelTimersTotal, wfKernelMemOwnerTask5=wfKernelMemOwnerTask5, wfKernelSysCfgSlot=wfKernelSysCfgSlot, wfKernelMemorySegsFree=wfKernelMemorySegsFree, wfKernelMemOwnerTask2=wfKernelMemOwnerTask2, wfKernelBufOwnerTask7=wfKernelBufOwnerTask7, wfKernParamLocMem=wfKernParamLocMem, wfKernelBufOwnerTask2Bufs=wfKernelBufOwnerTask2Bufs, wfKernCfgParamDelete=wfKernCfgParamDelete, wfKernelBufOwnerTask10Bufs=wfKernelBufOwnerTask10Bufs, wfKernCfgParamLocMem=wfKernCfgParamLocMem, wfKernelBufOwnerTask8=wfKernelBufOwnerTask8, wfKernelMemOwnerTask5Size=wfKernelMemOwnerTask5Size, wfKernelBufOwnerTask4=wfKernelBufOwnerTask4, wfKernelMemOwnerTask7=wfKernelMemOwnerTask7, wfKernelMemOwnerTask3Size=wfKernelMemOwnerTask3Size, wfKernCfgParamEntry=wfKernCfgParamEntry, wfKernelMemOwnerTask9Size=wfKernelMemOwnerTask9Size, wfKernelMemorySegsTotal=wfKernelMemorySegsTotal, wfKernelSysCfgEntry=wfKernelSysCfgEntry, wfKernelSysCfgLogging=wfKernelSysCfgLogging, wfKernCfgParamBufSize=wfKernCfgParamBufSize, wfKernelTable=wfKernelTable, wfKernelBufOwnerTask1=wfKernelBufOwnerTask1, wfKernelReplenEmpty=wfKernelReplenEmpty, wfKernCfgParamBufSizeReset=wfKernCfgParamBufSizeReset, wfKernelBufOwnerTask2=wfKernelBufOwnerTask2, wfKernelMemoryMaxSegFree=wfKernelMemoryMaxSegFree, wfKernelBufOwnerTask6=wfKernelBufOwnerTask6, wfKernelMemOwnerTask4=wfKernelMemOwnerTask4, wfKernelBufOwnerTask8Bufs=wfKernelBufOwnerTask8Bufs, wfKernelBufOwnerTask5=wfKernelBufOwnerTask5, wfKernCfgParamGlobMemReset=wfKernCfgParamGlobMemReset, wfKernelMemOwnerTask6Size=wfKernelMemOwnerTask6Size, wfKernelMemOwnerTask2Size=wfKernelMemOwnerTask2Size, wfKernelBufOwnerTask3Bufs=wfKernelBufOwnerTask3Bufs, wfKernelMemorySize=wfKernelMemorySize, wfKernParamGlobMem=wfKernParamGlobMem, wfKernelBuffersFree=wfKernelBuffersFree)
