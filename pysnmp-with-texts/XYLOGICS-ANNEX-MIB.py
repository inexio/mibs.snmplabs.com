#
# PySNMP MIB module XYLOGICS-ANNEX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLOGICS-ANNEX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:46:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibIdentifier, Gauge32, Bits, ModuleIdentity, Counter32, Counter64, Unsigned32, enterprises, iso, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Gauge32", "Bits", "ModuleIdentity", "Counter32", "Counter64", "Unsigned32", "enterprises", "iso", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xylogics = MibIdentifier((1, 3, 6, 1, 4, 1, 15))
prod = MibIdentifier((1, 3, 6, 1, 4, 1, 15, 1))
prodannex = MibScalar((1, 3, 6, 1, 4, 1, 15, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prodannex.setStatus('mandatory')
annex = MibIdentifier((1, 3, 6, 1, 4, 1, 15, 2))
hw = MibIdentifier((1, 3, 6, 1, 4, 1, 15, 2, 1))
sw = MibIdentifier((1, 3, 6, 1, 4, 1, 15, 2, 2))
ports = MibIdentifier((1, 3, 6, 1, 4, 1, 15, 2, 3))
hwType = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 11, 16, 23, 42, 52))).clone(namedValues=NamedValues(("err", 1), ("annexI", 11), ("annexII", 16), ("annexX25", 23), ("annex3", 42), ("microannex", 52)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwType.setStatus('mandatory')
hwRev = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwRev.setStatus('mandatory')
romRev = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: romRev.setStatus('mandatory')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('mandatory')
memorySize = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memorySize.setStatus('mandatory')
swType = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 11, 13, 16, 17, 23, 42, 43, 52))).clone(namedValues=NamedValues(("err", 1), ("annexImx", 11), ("annexIux", 13), ("annexIImx", 16), ("annexIIux", 17), ("annexX25", 23), ("annex3ux", 42), ("annex3mx", 43), ("microannexux", 52)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swType.setStatus('mandatory')
swRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRevMajor.setStatus('mandatory')
swRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRevMinor.setStatus('mandatory')
swBuild = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swBuild.setStatus('mandatory')
imageName = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imageName.setStatus('mandatory')
bootHost = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootHost.setStatus('mandatory')
defaultDomain = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defaultDomain.setStatus('mandatory')
currentDate = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentDate.setStatus('mandatory')
usableMemory = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usableMemory.setStatus('mandatory')
freeMemory = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: freeMemory.setStatus('mandatory')
minFreeMemory = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: minFreeMemory.setStatus('mandatory')
cpuUtilization = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilization.setStatus('mandatory')
maxProcs = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxProcs.setStatus('mandatory')
mostProcs = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mostProcs.setStatus('mandatory')
activeProcs = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: activeProcs.setStatus('mandatory')
cpuReschedsI = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuReschedsI.setStatus('mandatory')
cpuReschedsT = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuReschedsT.setStatus('mandatory')
contextSwI = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: contextSwI.setStatus('mandatory')
contextSwT = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: contextSwT.setStatus('mandatory')
cpuActivatesI = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuActivatesI.setStatus('mandatory')
cpuActivatesT = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuActivatesT.setStatus('mandatory')
cBlocksTotal = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBlocksTotal.setStatus('mandatory')
cBlocksFree = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBlocksFree.setStatus('mandatory')
cBlocksMinFree = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBlocksMinFree.setStatus('mandatory')
cBlocksDenied = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBlocksDenied.setStatus('mandatory')
maxCallouts = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxCallouts.setStatus('mandatory')
leastCallouts = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: leastCallouts.setStatus('mandatory')
freeCallouts = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 2, 28), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: freeCallouts.setStatus('mandatory')
totalPorts = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalPorts.setStatus('mandatory')
totalCharsIn = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalCharsIn.setStatus('mandatory')
totalCharsOut = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalCharsOut.setStatus('mandatory')
totalErrsParity = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalErrsParity.setStatus('mandatory')
totalErrsOverrun = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalErrsOverrun.setStatus('mandatory')
totalErrsFraming = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalErrsFraming.setStatus('mandatory')
portTable = MibTable((1, 3, 6, 1, 4, 1, 15, 2, 3, 7), )
if mibBuilder.loadTexts: portTable.setStatus('mandatory')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1), )
if mibBuilder.loadTexts: portEntry.setStatus('mandatory')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIndex.setStatus('mandatory')
iSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSpeed.setStatus('mandatory')
oSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oSpeed.setStatus('mandatory')
ctrlLines = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("dcddtr", 2), ("ctsrts", 3), ("both", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctrlLines.setStatus('mandatory')
flowTypeIn = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("xonxoff", 2), ("eia", 3), ("bell", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowTypeIn.setStatus('mandatory')
flowTypeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("xonxoff", 2), ("eia", 3), ("bell", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowTypeOut.setStatus('mandatory')
bitsPerChar = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("five", 1), ("six", 2), ("seven", 3), ("eight", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bitsPerChar.setStatus('mandatory')
stopBits = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("one", 1), ("onefive", 2), ("two", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stopBits.setStatus('mandatory')
parity = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("even", 2), ("odd", 3), ("mark", 4), ("space", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: parity.setStatus('mandatory')
modemDCD = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unused", 1), ("lo", 2), ("hi", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemDCD.setStatus('mandatory')
modemDTR = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unused", 1), ("lo", 2), ("hi", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemDTR.setStatus('mandatory')
modemCTS = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unused", 1), ("lo", 2), ("hi", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemCTS.setStatus('mandatory')
modemRTS = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unused", 1), ("lo", 2), ("hi", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemRTS.setStatus('mandatory')
charsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charsIn.setStatus('mandatory')
charsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charsOut.setStatus('mandatory')
errsParity = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errsParity.setStatus('mandatory')
errsOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errsOverrun.setStatus('mandatory')
errsFraming = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errsFraming.setStatus('mandatory')
inCC = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inCC.setStatus('mandatory')
outCC = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outCC.setStatus('mandatory')
mibBuilder.exportSymbols("XYLOGICS-ANNEX-MIB", contextSwT=contextSwT, swBuild=swBuild, bitsPerChar=bitsPerChar, annex=annex, maxProcs=maxProcs, mostProcs=mostProcs, cBlocksFree=cBlocksFree, freeCallouts=freeCallouts, iSpeed=iSpeed, portIndex=portIndex, totalErrsFraming=totalErrsFraming, flowTypeIn=flowTypeIn, hwType=hwType, xylogics=xylogics, memorySize=memorySize, modemCTS=modemCTS, modemRTS=modemRTS, errsParity=errsParity, prodannex=prodannex, swType=swType, leastCallouts=leastCallouts, totalCharsOut=totalCharsOut, charsOut=charsOut, defaultDomain=defaultDomain, cBlocksDenied=cBlocksDenied, cpuReschedsI=cpuReschedsI, totalPorts=totalPorts, totalErrsOverrun=totalErrsOverrun, errsOverrun=errsOverrun, charsIn=charsIn, totalErrsParity=totalErrsParity, portEntry=portEntry, hw=hw, totalCharsIn=totalCharsIn, cpuUtilization=cpuUtilization, contextSwI=contextSwI, cpuActivatesI=cpuActivatesI, flowTypeOut=flowTypeOut, minFreeMemory=minFreeMemory, errsFraming=errsFraming, imageName=imageName, ctrlLines=ctrlLines, cpuReschedsT=cpuReschedsT, sw=sw, cBlocksMinFree=cBlocksMinFree, swRevMinor=swRevMinor, activeProcs=activeProcs, portTable=portTable, oSpeed=oSpeed, freeMemory=freeMemory, cpuActivatesT=cpuActivatesT, prod=prod, maxCallouts=maxCallouts, cBlocksTotal=cBlocksTotal, usableMemory=usableMemory, ports=ports, hwRev=hwRev, currentDate=currentDate, parity=parity, serialNumber=serialNumber, romRev=romRev, modemDCD=modemDCD, modemDTR=modemDTR, inCC=inCC, stopBits=stopBits, outCC=outCC, bootHost=bootHost, swRevMajor=swRevMajor)
