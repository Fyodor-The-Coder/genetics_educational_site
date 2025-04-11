from django.db import migrations


def create_initial_terms(apps, schema_editor):
    term = apps.get_model('genetics_dictionary', 'Term')

    genetic_terms = [
        {
            'term_ru': 'Ген',
            'term_en': 'Gene',
            'term_definition': 'Основная единица наследственности, участок ДНК, кодирующий определённый белок или функциональную РНК.'
        },
        {
            'term_ru': 'Аллель',
            'term_en': 'Allele',
            'term_definition': 'Различные формы одного и того же гена, расположенные в одинаковых локусах гомологичных хромосом.'
        },
        {
            'term_ru': 'Хромосома',
            'term_en': 'Chromosome',
            'term_definition': 'Структура в ядре клетки, состоящая из ДНК и белков, несущая генетическую информацию.'
        },
        {
            'term_ru': 'ДНК',
            'term_en': 'DNA',
            'term_definition': 'Дезоксирибонуклеиновая кислота - молекула, хранящая генетические инструкции для развития и функционирования организмов.'
        },
        {
            'term_ru': 'РНК',
            'term_en': 'RNA',
            'term_definition': 'Рибонуклеиновая кислота, участвующая в реализации генетической информации через синтез белков.'
        },
        {
            'term_ru': 'Мутация',
            'term_en': 'Mutation',
            'term_definition': 'Постоянное изменение последовательности ДНК, которое может передаваться потомкам.'
        },
        {
            'term_ru': 'Транскрипция',
            'term_en': 'Transcription',
            'term_definition': 'Процесс синтеза РНК на матрице ДНК, происходящий в ядре клетки.'
        },
        {
            'term_ru': 'Трансляция',
            'term_en': 'Translation',
            'term_definition': 'Процесс синтеза белка на матрице иРНК с участием рибосом и тРНК.'
        },
        {
            'term_ru': 'Геном',
            'term_en': 'Genome',
            'term_definition': 'Полный набор генетического материала организма, включая все гены и некодирующие последовательности.'
        },
        {
            'term_ru': 'Генотип',
            'term_en': 'Genotype',
            'term_definition': 'Совокупность всех генов организма, определяющая его наследственные признаки.'
        },
        {
            'term_ru': 'Фенотип',
            'term_en': 'Phenotype',
            'term_definition': 'Совокупность наблюдаемых характеристик организма, формирующихся под влиянием генотипа и окружающей среды.'
        },
        {
            'term_ru': 'Гетерозигота',
            'term_en': 'Heterozygote',
            'term_definition': 'Организм, имеющий разные аллели одного гена в гомологичных хромосомах.'
        },
        {
            'term_ru': 'Гомозигота',
            'term_en': 'Homozygote',
            'term_definition': 'Организм, имеющий одинаковые аллели одного гена в гомологичных хромосомах.'
        },
        {
            'term_ru': 'Кодон',
            'term_en': 'Codon',
            'term_definition': 'Триплет нуклеотидов в ДНК или РНК, кодирующий определённую аминокислоту.'
        },
        {
            'term_ru': 'Рекомбинация',
            'term_en': 'Recombination',
            'term_definition': 'Процесс обмена генетическим материалом между гомологичными хромосомами во время мейоза.'
        },
        {
            'term_ru': 'Плазмида',
            'term_en': 'Plasmid',
            'term_definition': 'Небольшая кольцевая молекула ДНК у бактерий, часто используемая в генной инженерии.'
        },
        {
            'term_ru': 'Экспрессия гена',
            'term_en': 'Gene expression',
            'term_definition': 'Процесс реализации генетической информации от гена к функциональному белку.'
        },
        {
            'term_ru': 'Секвенирование',
            'term_en': 'Sequencing',
            'term_definition': 'Определение точной последовательности нуклеотидов в молекуле ДНК или РНК.'
        },
        {
            'term_ru': 'ПЦР',
            'term_en': 'PCR',
            'term_definition': 'Полимеразная цепная реакция - метод амплификации (копирования) определённых участков ДНК in vitro.'
        },
        {
            'term_ru': 'Эпигенетика',
            'term_en': 'Epigenetics',
            'term_definition': 'Изучение наследуемых изменений в экспрессии генов, не связанных с изменением последовательности ДНК.'
        },
        {
            'term_ru': 'Трансгенез',
            'term_en': 'Transgenesis',
            'term_definition': 'Процесс введения чужеродных генов в геном организма для получения новых свойств.'
        },
        {
            'term_ru': 'Генетический дрейф',
            'term_en': 'Genetic drift',
            'term_definition': 'Случайное изменение частот аллелей в популяции, особенно заметное в малых популяциях.'
        },
        {
            'term_ru': 'Сплайсинг',
            'term_en': 'Splicing',
            'term_definition': 'Процесс удаления интронов и соединения экзонов в молекуле пре-мРНК.'
        },
        {
            'term_ru': 'Генетический код',
            'term_en': 'Genetic code',
            'term_definition': 'Система соответствия между кодонами мРНК и аминокислотами в синтезируемом белке.'
        },
        {
            'term_ru': 'Плейотропия',
            'term_en': 'Pleiotropy',
            'term_definition': 'Явление, при котором один ген влияет на несколько фенотипических признаков.'
        },
        {
            'term_ru': 'Эпистаз',
            'term_en': 'Epistasis',
            'term_definition': 'Взаимодействие генов, при котором один ген подавляет проявление другого гена.'
        },
        {
            'term_ru': 'Нонсенс-мутация',
            'term_en': 'Nonsense mutation',
            'term_definition': 'Мутация, приводящая к образованию стоп-кодона и преждевременному окончанию синтеза белка.'
        },
        {
            'term_ru': 'Соматическая мутация',
            'term_en': 'Somatic mutation',
            'term_definition': 'Мутация, возникающая в клетках тела и не передающаяся потомству.'
        },
        {
            'term_ru': 'Клонирование',
            'term_en': 'Cloning',
            'term_definition': 'Процесс создания генетически идентичных копий биологических организмов или их фрагментов.'
        },
        {
            'term_ru': 'Популяционная генетика',
            'term_en': 'Population genetics',
            'term_definition': 'Раздел генетики, изучающий распределение и изменение частот генов в популяциях.'
        },
        {
            'term_ru': 'Генетическая инженерия',
            'term_en': 'Genetic engineering',
            'term_definition': 'Совокупность технологий для изменения генетического материала организмов.'
        }
    ]

    terms_to_create = [
        term(**term_data)
        for term_data in genetic_terms
    ]
    term.objects.bulk_create(terms_to_create)


class Migration(migrations.Migration):
    dependencies = [
        ('genetics_dictionary', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_initial_terms,
            reverse_code=migrations.RunPython.noop
        )
    ]