#
# PySNMP MIB module HH3C-MPLSOAM-PS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-MPLSOAM-PS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:28:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, ModuleIdentity, Gauge32, Unsigned32, NotificationType, ObjectIdentity, IpAddress, MibIdentifier, iso, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "ModuleIdentity", "Gauge32", "Unsigned32", "NotificationType", "ObjectIdentity", "IpAddress", "MibIdentifier", "iso", "Integer32", "TimeTicks")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
hh3cMplsOamPs = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 80))
if mibBuilder.loadTexts: hh3cMplsOamPs.setLastUpdated('200703310000Z')
if mibBuilder.loadTexts: hh3cMplsOamPs.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cMplsOamPs.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cMplsOamPs.setDescription('This MIB contains objects to configure mpls protect-switch module.')
hh3cMplsOamPsScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 80, 1))
hh3cMplsOamPsTrapOpen = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 80, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMplsOamPsTrapOpen.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsOamPsTrapOpen.setDescription('Whether mpls protect-switch trap is globally enabled. false: disable; true: enable')
hh3cMplsOamPsTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2))
hh3cMplsPsTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1), )
if mibBuilder.loadTexts: hh3cMplsPsTable.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsTable.setDescription('This table specifies per-protection-group MPLS PS capability and associated information.')
hh3cMplsPsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1), ).setIndexNames((0, "HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsIndex"))
if mibBuilder.loadTexts: hh3cMplsPsEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsEntry.setDescription('An entry in this table is created by an LSR for every protection group capable of supporting mpls ps.')
hh3cMplsPsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cMplsPsIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsIndex.setDescription('This is a unique index for an entry in the mplspsEntry.')
hh3cMplsPsGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMplsPsGroupID.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsGroupID.setDescription('This is a unique group id for an entry in the mplspsEntry. One protect-switch group is composed of one working static-lsp and one protection static-lsp.')
hh3cMplsPsWorkLspName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 3), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMplsPsWorkLspName.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsWorkLspName.setDescription('The name of the working static-lsp.')
hh3cMplsPsProtectLspName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 4), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMplsPsProtectLspName.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsProtectLspName.setDescription('The name of the protection static-lsp.')
hh3cMplsPsRevertiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMplsPsRevertiveMode.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsRevertiveMode.setDescription('Revertive mode is a protection switching mode where revertive action (switch back to the working LSP) is taken after the working LSP is repaired. And switching does not occur in a non-revertive mode. 1: revertive; 2: non-revertive;')
hh3cMplsPsWTR = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 6), Integer32()).setUnits('30s').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMplsPsWTR.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsWTR.setDescription('Wait to Restore timer is only applicable for the revertive mode and applies to a working LSP, it prevents reversion back to select the working LSP until the Wait to Restore timer has expired. The default value is 12 minutes. step is 30s.')
hh3cMplsPsHoldOff = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 7), Integer32()).setUnits('100ms').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMplsPsHoldOff.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsHoldOff.setDescription('The time between declaration of signal degrade or signal fail, and the initialization of the protection switching algorithm. Step is 100ms, maximum is 10s.')
hh3cMplsPsSwitchCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMplsPsSwitchCondition.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsSwitchCondition.setDescription('The current switch condition of the protection group. 1: clear, this command clears all of the externally initiated switch commands listed below; 2: lockout of protection, fix the selector position on the working LSP, Prevents the selector from switching to the protection LSP when it is selecting the working LSP. Switches the selector from the protection to the working LSP when it is selecting the protection LSP; 3: forced protection, switches the selector from the working LSP to the protection LSP (unless a higher priority switch request (i.e., LoP) is in effect); 4: signal fail, for 1:1, Signal Fail (SF) is declared when the source of the protection domain enters the Defect State by receiving a BDI packet (from the return LSP or out of band). 5: manual switch for working-lsp, switches the selector from the working LSP to the protection LSP (unless an equal or higher priority switch request (i.e., LoP, FS, SF or MS) is in effect); 6: manual switch for protection-lsp, switches the selector from the protection LSP to the working LSP (unless an equal or higher priority switch request (i.e., LoP, FS, SF or MS) is in effect). 7: WTR-timer, a configurable timer which is used to delay before reversion; 8: HoldOff-timer, the time between declaration of signal degrade or signal fail, and the initialization of the protection switching algorithm; 9: Others; The pripority of the commands are: clear > lockout of protection > force switch > manual switch for working lsp = manual switch for protection lsp')
hh3cMplsPsWorkLspDetectState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMplsPsWorkLspDetectState.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsWorkLspDetectState.setDescription('The state of working static-lsp state in one protection group, whether it is in defect: 1: it is out of defect; 2: it enters defect.')
hh3cMplsPsWorkLspUpDownState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMplsPsWorkLspUpDownState.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsWorkLspUpDownState.setDescription('The state of working static-lsp state in one protection group, whether it is up or down: 1: it is in up state; 2: it is in down state.')
hh3cMplsPsProtLspDetectState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMplsPsProtLspDetectState.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsProtLspDetectState.setDescription('The state of protection static-lsp state in one protection group, whether it is in detection: 1: it is out of defect; 2: it enters defect.')
hh3cMplsPsProtLspUpDownState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMplsPsProtLspUpDownState.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsProtLspUpDownState.setDescription('The state of protection static-lsp state in one protection group, whether it is up or down: 1: it is in up state; 2: it is in down state.')
hh3cMplsPsSwitchResult = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMplsPsSwitchResult.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsSwitchResult.setDescription('Which tunnel is used to transfer the data stream. 1: working static-lsp; 2: protection static-lsp.')
hh3cMplsPsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMplsPsRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsRowStatus.setDescription('This object is responsible for managing the creation, deletion and modification of rows, which support active status and CreatAndGo, destroy operation. To create a new row, hh3cMplsPsGroupID, hh3cMplsPsWorkLspName, hh3cMplsPsProtectLspName, hh3cMplsPsRevertiveMode, hh3cMplsPsWTR and hh3cMplsPsHoldOff must be specified.')
hh3cMplsOamPsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 80, 3))
hh3cMplsPsSwitchPtoW = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 80, 3, 1)).setObjects(("HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsWorkLspName"), ("HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsProtectLspName"), ("HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsSwitchResult"))
if mibBuilder.loadTexts: hh3cMplsPsSwitchPtoW.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsSwitchPtoW.setDescription('This notification is generated when switching from protection-lsp to working-lsp occured.')
hh3cMplsPsSwitchWtoP = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 80, 3, 2)).setObjects(("HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsWorkLspName"), ("HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsProtectLspName"), ("HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsSwitchResult"))
if mibBuilder.loadTexts: hh3cMplsPsSwitchWtoP.setStatus('current')
if mibBuilder.loadTexts: hh3cMplsPsSwitchWtoP.setDescription('This notification is generated when switching from woking-lsp to protection-lsp occured.')
mibBuilder.exportSymbols("HH3C-MPLSOAM-PS-MIB", hh3cMplsPsIndex=hh3cMplsPsIndex, hh3cMplsPsEntry=hh3cMplsPsEntry, hh3cMplsOamPsScalarGroup=hh3cMplsOamPsScalarGroup, hh3cMplsPsWorkLspUpDownState=hh3cMplsPsWorkLspUpDownState, hh3cMplsPsProtLspDetectState=hh3cMplsPsProtLspDetectState, hh3cMplsPsRevertiveMode=hh3cMplsPsRevertiveMode, hh3cMplsPsSwitchWtoP=hh3cMplsPsSwitchWtoP, hh3cMplsOamPs=hh3cMplsOamPs, hh3cMplsOamPsNotifications=hh3cMplsOamPsNotifications, hh3cMplsPsRowStatus=hh3cMplsPsRowStatus, hh3cMplsPsWorkLspName=hh3cMplsPsWorkLspName, hh3cMplsPsTable=hh3cMplsPsTable, hh3cMplsPsSwitchPtoW=hh3cMplsPsSwitchPtoW, hh3cMplsPsWorkLspDetectState=hh3cMplsPsWorkLspDetectState, PYSNMP_MODULE_ID=hh3cMplsOamPs, hh3cMplsPsWTR=hh3cMplsPsWTR, hh3cMplsOamPsTrapOpen=hh3cMplsOamPsTrapOpen, hh3cMplsPsHoldOff=hh3cMplsPsHoldOff, hh3cMplsPsSwitchResult=hh3cMplsPsSwitchResult, hh3cMplsOamPsTable=hh3cMplsOamPsTable, hh3cMplsPsProtectLspName=hh3cMplsPsProtectLspName, hh3cMplsPsSwitchCondition=hh3cMplsPsSwitchCondition, hh3cMplsPsGroupID=hh3cMplsPsGroupID, hh3cMplsPsProtLspUpDownState=hh3cMplsPsProtLspUpDownState)