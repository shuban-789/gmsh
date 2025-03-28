#!/usr/bin/python3
import gmsh
import numpy as np

gmsh.initialize()
gmsh.model.add("simple")

size = 0.01
gmsh.model.geo.addPoint(0.0, 0.0, 0.0, size, 1)
gmsh.model.geo.addPoint(0.1, 0.0, 0.0, size, 2)
gmsh.model.geo.addPoint(0.1, 0.1, 0.0, size, 3)
gmsh.model.geo.addPoint(0.0, 0.1, 0.0, size, 4)
gmsh.model.geo.addPoint(0.009999999999982483, 0.0, 0.0, size, 5)
gmsh.model.geo.addPoint(0.019999999999956, 0.0, 0.0, size, 6)
gmsh.model.geo.addPoint(0.02999999999992728, 0.0, 0.0, size, 7)
gmsh.model.geo.addPoint(0.03999999999989585, 0.0, 0.0, size, 8)
gmsh.model.geo.addPoint(0.0499999999998685, 0.0, 0.0, size, 9)
gmsh.model.geo.addPoint(0.05999999999989426, 0.0, 0.0, size, 10)
gmsh.model.geo.addPoint(0.06999999999991974, 0.0, 0.0, size, 11)
gmsh.model.geo.addPoint(0.07999999999994738, 0.0, 0.0, size, 12)
gmsh.model.geo.addPoint(0.08999999999997287, 0.0, 0.0, size, 13)
gmsh.model.geo.addPoint(0.1, 0.009999999999982483, 0.0, size, 14)
gmsh.model.geo.addPoint(0.1, 0.019999999999956, 0.0, size, 15)
gmsh.model.geo.addPoint(0.1, 0.02999999999992728, 0.0, size, 16)
gmsh.model.geo.addPoint(0.1, 0.03999999999989585, 0.0, size, 17)
gmsh.model.geo.addPoint(0.1, 0.0499999999998685, 0.0, size, 18)
gmsh.model.geo.addPoint(0.1, 0.05999999999989426, 0.0, size, 19)
gmsh.model.geo.addPoint(0.1, 0.06999999999991974, 0.0, size, 20)
gmsh.model.geo.addPoint(0.1, 0.07999999999994738, 0.0, size, 21)
gmsh.model.geo.addPoint(0.1, 0.08999999999997287, 0.0, size, 22)
gmsh.model.geo.addPoint(0.09000000000002764, 0.1, 0.0, size, 23)
gmsh.model.geo.addPoint(0.08000000000005529, 0.1, 0.0, size, 24)
gmsh.model.geo.addPoint(0.07000000000008294, 0.1, 0.0, size, 25)
gmsh.model.geo.addPoint(0.06000000000011058, 0.1, 0.0, size, 26)
gmsh.model.geo.addPoint(0.05000000000013687, 0.1, 0.0, size, 27)
gmsh.model.geo.addPoint(0.04000000000011003, 0.1, 0.0, size, 28)
gmsh.model.geo.addPoint(0.03000000000008349, 0.1, 0.0, size, 29)
gmsh.model.geo.addPoint(0.02000000000005478, 0.1, 0.0, size, 30)
gmsh.model.geo.addPoint(0.01000000000002821, 0.1, 0.0, size, 31)
gmsh.model.geo.addPoint(0.0, 0.09000000000002764, 0.0, size, 32)
gmsh.model.geo.addPoint(0.0, 0.08000000000005529, 0.0, size, 33)
gmsh.model.geo.addPoint(0.0, 0.07000000000008294, 0.0, size, 34)
gmsh.model.geo.addPoint(0.0, 0.06000000000011058, 0.0, size, 35)
gmsh.model.geo.addPoint(0.0, 0.05000000000013687, 0.0, size, 36)
gmsh.model.geo.addPoint(0.0, 0.04000000000011003, 0.0, size, 37)
gmsh.model.geo.addPoint(0.0, 0.03000000000008349, 0.0, size, 38)
gmsh.model.geo.addPoint(0.0, 0.02000000000005478, 0.0, size, 39)
gmsh.model.geo.addPoint(0.0, 0.01000000000002821, 0.0, size, 40)
gmsh.model.geo.addPoint(0.008660254037844496, 0.04500000000012346, 0.0, size, 41)
gmsh.model.geo.addPoint(0.05394257192623655, 0.009236792741080668, 0.0, size, 42)
gmsh.model.geo.addPoint(0.09133974596215644, 0.05499999999988138, 0.0, size, 43)
gmsh.model.geo.addPoint(0.04531597093726643, 0.09152217186777929, 0.0, size, 44)
gmsh.model.geo.addPoint(0.03490798000978403, 0.008885430207218782, 0.0, size, 45)
gmsh.model.geo.addPoint(0.09133974596218283, 0.03499999999991157, 0.0, size, 46)
gmsh.model.geo.addPoint(0.008660254037828075, 0.06500000000008696, 0.0, size, 47)
gmsh.model.geo.addPoint(0.06500000000009674, 0.09133974596217956, 0.0, size, 48)
gmsh.model.geo.addPoint(0.07482623088808088, 0.007629831345361252, 0.0, size, 49)
gmsh.model.geo.addPoint(0.008613067098680056, 0.0250817301762179, 0.0, size, 50)
gmsh.model.geo.addPoint(0.09204077431034642, 0.074597880323163, 0.0, size, 51)
gmsh.model.geo.addPoint(0.02413274345296874, 0.09103703875044512, 0.0, size, 52)
gmsh.model.geo.addPoint(0.01591825619056905, 0.009056972474446692, 0.0, size, 53)
gmsh.model.geo.addPoint(0.09045047171895057, 0.01554440545897103, 0.0, size, 54)
gmsh.model.geo.addPoint(0.00846772045054154, 0.08495762630722971, 0.0, size, 55)
gmsh.model.geo.addPoint(0.08494067683010678, 0.09170502595852396, 0.0, size, 56)
gmsh.model.geo.addPoint(0.008652389547988384, 0.03501362169613298, 0.0, size, 57)
gmsh.model.geo.addPoint(0.01731919732737425, 0.04000227028279618, 0.0, size, 58)
gmsh.model.geo.addPoint(0.01732028961762058, 0.05000037838055285, 0.0, size, 59)
gmsh.model.geo.addPoint(0.02598050724577564, 0.04500044144397573, 0.0, size, 60)
gmsh.model.geo.addPoint(0.02598068322586638, 0.05500013663748059, 0.0, size, 61)
gmsh.model.geo.addPoint(0.03464096052543003, 0.05000009634698678, 0.0, size, 62)
gmsh.model.geo.addPoint(0.03460375899349638, 0.03996660322677582, 0.0, size, 63)
gmsh.model.geo.addPoint(0.0432586763287336, 0.04492890262145871, 0.0, size, 64)
gmsh.model.geo.addPoint(0.04329416194142583, 0.05498816649480558, 0.0, size, 65)
gmsh.model.geo.addPoint(0.05195324054227968, 0.04998617818612668, 0.0, size, 66)
gmsh.model.geo.addPoint(0.05195895890489637, 0.05999572411354738, 0.0, size, 67)
gmsh.model.geo.addPoint(0.05191666957299501, 0.03992029949377892, 0.0, size, 68)
gmsh.model.geo.addPoint(0.06061292187501574, 0.044984412946745, 0.0, size, 69)
gmsh.model.geo.addPoint(0.06055738768621194, 0.03508014145105813, 0.0, size, 70)
gmsh.model.geo.addPoint(0.04329965792750854, 0.06499731510143872, 0.0, size, 71)
gmsh.model.geo.addPoint(0.05163390725853734, 0.07044542185658814, 0.0, size, 72)
gmsh.model.geo.addPoint(0.06056674788303687, 0.06507352432841577, 0.0, size, 73)
gmsh.model.geo.addPoint(0.05192180217588005, 0.02989417123120785, 0.0, size, 74)
gmsh.model.geo.addPoint(0.06926982447455876, 0.04001075906640617, 0.0, size, 75)
gmsh.model.geo.addPoint(0.06930152412634935, 0.03026306839244985, 0.0, size, 76)
gmsh.model.geo.addPoint(0.06927852159964032, 0.04999919533560718, 0.0, size, 77)
gmsh.model.geo.addPoint(0.07794228634044036, 0.04500000000014998, 0.0, size, 78)
gmsh.model.geo.addPoint(0.04298696763616039, 0.07516124797966264, 0.0, size, 79)
gmsh.model.geo.addPoint(0.03458836368221107, 0.07002642718022548, 0.0, size, 80)
gmsh.model.geo.addPoint(0.06012745329117123, 0.0753535810939433, 0.0, size, 81)
gmsh.model.geo.addPoint(0.06928203230261039, 0.07000000000007785, 0.0, size, 82)
gmsh.model.geo.addPoint(0.03464101615130891, 0.08000000000004234, 0.0, size, 83)
gmsh.model.geo.addPoint(0.02613945494723902, 0.07471434102061028, 0.0, size, 84)
gmsh.model.geo.addPoint(0.0779422863404322, 0.05500000000012545, 0.0, size, 85)
gmsh.model.geo.addPoint(0.06952463901855788, 0.08109810542583701, 0.0, size, 86)
gmsh.model.geo.addPoint(0.07784372413937804, 0.07487737367123214, 0.0, size, 87)
gmsh.model.geo.addPoint(0.0173111143794831, 0.03001627035926538, 0.0, size, 88)
gmsh.model.geo.addPoint(0.01703018238311188, 0.01994089234451431, 0.0, size, 89)
gmsh.model.geo.addPoint(0.02589421166479641, 0.02499286045075582, 0.0, size, 90)
gmsh.model.geo.addPoint(0.02568398517527755, 0.01494939110576759, 0.0, size, 91)
gmsh.model.geo.addPoint(0.03465136387854947, 0.01967429917976695, 0.0, size, 92)
gmsh.model.geo.addPoint(0.04403108432718279, 0.0147506470839471, 0.0, size, 93)
gmsh.model.geo.addPoint(0.04352414774239571, 0.02461396475419542, 0.0, size, 94)
gmsh.model.geo.addPoint(0.0526116478758601, 0.02006125504554324, 0.0, size, 95)
gmsh.model.geo.addPoint(0.06196113524642624, 0.01629581819750722, 0.0, size, 96)
gmsh.model.geo.addPoint(0.04327441461018586, 0.03488732355460585, 0.0, size, 97)
gmsh.model.geo.addPoint(0.03471016110712712, 0.08994183955993519, 0.0, size, 98)
gmsh.model.geo.addPoint(0.09133974596213583, 0.06499999999991302, 0.0, size, 99)
gmsh.model.geo.addPoint(0.01732045851805086, 0.06000008583639127, 0.0, size, 100)
gmsh.model.geo.addPoint(0.05505266182297407, 0.09157740970141273, 0.0, size, 101)
gmsh.model.geo.addPoint(0.05100182665275212, 0.08167956118737357, 0.0, size, 102)
gmsh.model.geo.addPoint(0.09133974596215921, 0.04499999999990038, 0.0, size, 103)
gmsh.model.geo.addPoint(0.008660209368557333, 0.055000077369567, 0.0, size, 104)
gmsh.model.geo.addPoint(0.07794228634044713, 0.03500000000017538, 0.0, size, 105)
gmsh.model.geo.addPoint(0.07794228634045706, 0.02500000000019326, 0.0, size, 106)
gmsh.model.geo.addPoint(0.09184537499730142, 0.02540998849578394, 0.0, size, 107)
gmsh.model.geo.addPoint(0.06060873718457927, 0.05500650581842424, 0.0, size, 108)
gmsh.model.geo.addPoint(0.03463076490265551, 0.06000202362683481, 0.0, size, 109)
gmsh.model.geo.addPoint(0.01734694862167957, 0.0699524044762107, 0.0, size, 110)
gmsh.model.geo.addPoint(0.06927010194178891, 0.06001320424712472, 0.0, size, 111)
gmsh.model.geo.addPoint(0.02600111231628373, 0.06494923646295885, 0.0, size, 112)
gmsh.model.geo.addPoint(0.01817472487888312, 0.08150627101358082, 0.0, size, 113)
gmsh.model.geo.addPoint(0.07491088597482581, 0.0913246981744902, 0.0, size, 114)
gmsh.model.geo.addPoint(0.008774941331488716, 0.07523605029954106, 0.0, size, 115)
gmsh.model.geo.addPoint(0.07794228634043451, 0.0650000000000979, 0.0, size, 116)
gmsh.model.geo.addPoint(0.02592170374309002, 0.03499640762729789, 0.0, size, 117)
gmsh.model.geo.addPoint(0.03464493343875231, 0.02985524313223296, 0.0, size, 118)
gmsh.model.geo.addPoint(0.008212753751736508, 0.01530678781039284, 0.0, size, 119)
gmsh.model.geo.addPoint(0.08465660393049619, 0.007782069516417631, 0.0, size, 120)
gmsh.model.geo.addPoint(0.0149134061183952, 0.0916756321701239, 0.0, size, 121)
gmsh.model.geo.addPoint(0.0906145656023098, 0.08440933898606122, 0.0, size, 122)
gmsh.model.geo.addPoint(0.06066557748396734, 0.02549526979401031, 0.0, size, 123)
gmsh.model.geo.addPoint(0.064999999999907, 0.007664186808191014, 0.0, size, 124)
gmsh.model.geo.addPoint(0.06988638159712106, 0.02113197087423403, 0.0, size, 125)
gmsh.model.geo.addPoint(0.08000000000005525, 0.08380531170040062, 0.0, size, 126)
gmsh.model.geo.addPoint(0.07883818970859875, 0.01607768562198898, 0.0, size, 127)
gmsh.model.geo.addPoint(0.06007210008021557, 0.08406928938273674, 0.0, size, 128)
gmsh.model.geo.addPoint(0.02530204427510278, 0.006578358757486612, 0.0, size, 129)
gmsh.model.geo.addPoint(0.08464101615138538, 0.05999999999988339, 0.0, size, 130)
gmsh.model.geo.addPoint(0.08464101615135418, 0.06999999999992175, 0.0, size, 131)
gmsh.model.geo.addPoint(0.08464101615139293, 0.04999999999988895, 0.0, size, 132)
gmsh.model.geo.addPoint(0.08464101615139413, 0.03999999999991675, 0.0, size, 133)
gmsh.model.geo.addPoint(0.08464101615141345, 0.02999999999992713, 0.0, size, 134)
gmsh.model.geo.addPoint(0.0269855715851136, 0.08325961894323256, 0.0, size, 135)
gmsh.model.geo.addPoint(0.04499999999988217, 0.006525626353141744, 0.0, size, 136)
gmsh.model.geo.addPoint(0.04173118849692299, 0.08366096411895861, 0.0, size, 137)
gmsh.model.geo.addPoint(0.09267949192432309, 0.007320508075664961, 0.0, size, 138)
gmsh.model.geo.addPoint(0.007320508075664806, 0.007320508075677057, 0.0, size, 139)
gmsh.model.geo.addPoint(0.09267949192434079, 0.09267949192432605, 0.0, size, 140)
gmsh.model.geo.addPoint(0.007320508075674081, 0.09267949192434094, 0.0, size, 141)
gmsh.model.geo.addPoint(0.06946433733382396, 0.01353999664273501, 0.0, size, 142)
gmsh.model.geo.addPoint(0.08474346778334424, 0.02240641591537287, 0.0, size, 143)
gmsh.model.geo.addPoint(0.08502801604068873, 0.07753798093615574, 0.0, size, 144)

gmsh.model.geo.addLine(1, 5, 1)
gmsh.model.geo.addLine(5, 6, 2)
gmsh.model.geo.addLine(6, 7, 3)
gmsh.model.geo.addLine(7, 8, 4)
gmsh.model.geo.addLine(8, 9, 5)
gmsh.model.geo.addLine(9, 10, 6)
gmsh.model.geo.addLine(10, 11, 7)
gmsh.model.geo.addLine(11, 12, 8)
gmsh.model.geo.addLine(12, 13, 9)
gmsh.model.geo.addLine(13, 2, 10)
gmsh.model.geo.addLine(2, 14, 11)
gmsh.model.geo.addLine(14, 15, 12)
gmsh.model.geo.addLine(15, 16, 13)
gmsh.model.geo.addLine(16, 17, 14)
gmsh.model.geo.addLine(17, 18, 15)
gmsh.model.geo.addLine(18, 19, 16)
gmsh.model.geo.addLine(19, 20, 17)
gmsh.model.geo.addLine(20, 21, 18)
gmsh.model.geo.addLine(21, 22, 19)
gmsh.model.geo.addLine(22, 3, 20)
gmsh.model.geo.addLine(4, 32, 21)
gmsh.model.geo.addLine(32, 33, 22)
gmsh.model.geo.addLine(33, 34, 23)
gmsh.model.geo.addLine(34, 35, 24)
gmsh.model.geo.addLine(35, 36, 25)
gmsh.model.geo.addLine(36, 37, 26)
gmsh.model.geo.addLine(37, 38, 27)
gmsh.model.geo.addLine(38, 39, 28)
gmsh.model.geo.addLine(39, 40, 29)
gmsh.model.geo.addLine(40, 1, 30)

gmsh.model.geo.addCurveLoop([np.uint64(1), np.uint64(2), np.uint64(3), np.uint64(4), np.uint64(5), np.uint64(6), np.uint64(7), np.uint64(8), np.uint64(9), np.uint64(10), np.uint64(11), np.uint64(12), np.uint64(13), np.uint64(14), np.uint64(15), np.uint64(16), np.uint64(17), np.uint64(18), np.uint64(19), np.uint64(20), np.uint64(21), np.uint64(22), np.uint64(23), np.uint64(24), np.uint64(25), np.uint64(26), np.uint64(27), np.uint64(28), np.uint64(29), np.uint64(30)], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.synchronize()

# gmsh.model.addPhysicalGroup(1, [1 2 4], 5)  --> Should be: gmsh.model.addPhysicalGroup(1, [1, 2, 4], 5)
gmsh.model.addPhysicalGroup(1, [1, 2, 4], 5)
gmsh.model.addPhysicalGroup(2, [1], name="Write Upon This Mesh via UI")

gmsh.model.mesh.generate(2)
gmsh.finalize()
